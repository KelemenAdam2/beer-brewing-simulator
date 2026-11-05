import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QAbstractItemView, QHeaderView
from PySide6.QtCore import Qt, QTimer, QEventLoop

from src.core.model import Malt, Hop, Yeast
from src.ui.pyside_ui.ui_form import Ui_MainWindow
from src.core.repository import Repository
from src.core.recipe import Recipe
from src.ui.pyside_ui.simulation_widget import SimulationVesselWidget, draw_simulation

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Core logic models
        self.repo = Repository()
        self.recipe = Recipe()
        self.flags = {
            "US": "🇺🇸",
            "UK": "🇬🇧",
            "Germany": "🇩🇪",
            "Belgium": "🇧🇪",
            "Czech Republic": "🇨🇿",
            "Australia": "🇦🇺",
            "New Zealand": "🇳🇿",
            "France": "🇫🇷",
            "Canada": "🇨🇦",
            "Poland": "🇵🇱",
            "Slovenia": "🇸🇮",
            "Japan": "🇯🇵",
        }
        self.stage = 0
        self.current_stage = 0

        # Timeline
        self.is_playing = False
        self.playback_rate = 0
        self.timeline_timer = QTimer(self)
        self.mashing_end = 12000
        self.boiling_end = 12000
        self.fermenting_end = 3000

        # Simulation visual vessels
        self.vessel_mashing = SimulationVesselWidget(self.ui.widget_mashing)
        self.ui.horizontalLayout_5.addWidget(self.vessel_mashing)

        self.vessel_boiling = SimulationVesselWidget(self.ui.widget_boiling)
        self.ui.horizontalLayout_6.addWidget(self.vessel_boiling)

        self.vessel_fermenting = SimulationVesselWidget(self.ui.widget_fermenting)
        self.ui.horizontalLayout_4.addWidget(self.vessel_fermenting)

        # Wire up data and events
        self.init_data()
        self.init_sim()
        self.connect_signals()
        self.info_help()
        self.showMaximized()

    def init_data(self):
        # 1. Populate Malts
        malts = self.repo.get_malts()
        self.ui.tbl_malts.clear()
        self.ui.tbl_malts.setColumnCount(4)
        self.ui.tbl_malts.setHorizontalHeaderLabels(["Origin", "Name", "Color", "Potential"])
        self.ui.tbl_malts.setRowCount(len(malts))
        self.ui.tbl_malts.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.ui.tbl_malts.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.ui.tbl_malts.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.ui.tbl_malts.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.ui.tbl_yeasts.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        for row, malt in enumerate(malts):
            flag = QTableWidgetItem(" ")
            font = flag.font()
            font.setPointSize(30)
            flag.setFont(font)
            flag.setText(self.flags[malt.origin])
            self.ui.tbl_malts.setItem(row, 0, flag)
            self.ui.tbl_malts.setItem(row, 1, QTableWidgetItem(str(malt.name)))
            self.ui.tbl_malts.setItem(row, 2, QTableWidgetItem(str(malt.color)))
            self.ui.tbl_malts.setItem(row, 3, QTableWidgetItem(str(malt.potential)))

        # 2. Populate Hops
        hops = self.repo.get_hops()
        self.ui.tbl_hops.clear()
        self.ui.tbl_hops.setColumnCount(5)
        self.ui.tbl_hops.setHorizontalHeaderLabels(["Origin", "Name", "Type", "Alpha", "Beta"])
        self.ui.tbl_hops.setRowCount(len(hops))
        self.ui.tbl_hops.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.ui.tbl_hops.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.ui.tbl_hops.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.ui.tbl_hops.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.ui.tbl_yeasts.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        for row, hop in enumerate(hops):
            flag = QTableWidgetItem(" ")
            font = flag.font()
            font.setPointSize(30)
            flag.setFont(font)
            flag.setText(self.flags[hop.origin])
            self.ui.tbl_hops.setItem(row, 0, flag)
            self.ui.tbl_hops.setItem(row, 1, QTableWidgetItem(str(hop.name)))
            self.ui.tbl_hops.setItem(row, 2, QTableWidgetItem(str(hop.type)))
            self.ui.tbl_hops.setItem(row, 3, QTableWidgetItem(str(hop.alpha)))
            self.ui.tbl_hops.setItem(row, 4, QTableWidgetItem(str(hop.beta)))

        # 3. Populate Yeasts
        yeasts = self.repo.get_yeasts()
        self.ui.tbl_yeasts.clear()
        self.ui.tbl_yeasts.setColumnCount(7)
        self.ui.tbl_yeasts.setHorizontalHeaderLabels(["Name", "Lab", "Form", "Type", "Temp", "Att.", "Floc."])
        self.ui.tbl_yeasts.setRowCount(len(yeasts))
        self.ui.tbl_yeasts.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.ui.tbl_yeasts.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.ui.tbl_yeasts.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.ui.tbl_yeasts.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.ui.tbl_yeasts.horizontalHeader().setSectionResizeMode(0,QHeaderView.ResizeMode.Stretch)
        for row, yeast in enumerate(yeasts):
            self.ui.tbl_yeasts.setItem(row, 0, QTableWidgetItem(str(yeast.name)))
            self.ui.tbl_yeasts.setItem(row, 1, QTableWidgetItem(str(yeast.lab)))
            self.ui.tbl_yeasts.setItem(row, 2, QTableWidgetItem(str(yeast.form)))
            self.ui.tbl_yeasts.setItem(row, 3, QTableWidgetItem(str(yeast.type)))
            self.ui.tbl_yeasts.setItem(row, 4, QTableWidgetItem(f"{yeast.min_temp}˚C - {yeast.max_temp}˚C"))
            self.ui.tbl_yeasts.setItem(row, 5, QTableWidgetItem(f"{yeast.attenuation * 100:.0f}%"))
            self.ui.tbl_yeasts.setItem(row, 6, QTableWidgetItem(str(yeast.flocculation)))

        # 4. Set defaults for sliders and inputs
        self.ui.slider_malt_weight.setRange(1, 100)   # 0.1 kg to 10.0 kg
        self.ui.slider_malt_weight.setValue(40)        # default 4.0 kg
        self.ui.edit_malt_weight.setText("4.0 kg")

        self.ui.slider_hop_weight.setRange(1, 100)    # 1g to 100g
        self.ui.slider_hop_weight.setValue(30)        # default 30g
        self.ui.edit_hop_weight.setText("30 g")

        self.ui.slider_hop_time.setRange(0, 120)      # 0 to 120 mins
        self.ui.slider_hop_time.setValue(60)          # default 60 mins
        self.ui.edit_hop_time.setText("60 min")

        self.ui.edit_summary_water.setText("0 L")
        self.recipe.current_water = 0.0

        # Select first items if available
        if self.ui.tbl_malts.rowCount() > 0:
            self.ui.tbl_malts.selectRow(0)
        if self.ui.tbl_hops.rowCount() > 0:
            self.ui.tbl_hops.selectRow(0)
        if self.ui.tbl_yeasts.rowCount() > 0:
            self.ui.tbl_yeasts.selectRow(0)

        self.refresh_metrics()
        self.ui.tab_widget_ingredients.tabBar().setEnabled(False)

    def init_sim(self):
        self.stage = 0
        self.ui.lbl_brewing_stage_title.setText("Mashing")
        self.ui.btn_brewing_stage_prev.setEnabled(False)
        self.ui.btn_brewing_stage_next.setEnabled(True)
        self.ui.tab_widget_ingredients.setCurrentIndex(self.stage)
        self.ui.stacked_widget_stage.setCurrentIndex(self.stage)
        self.set_up_timeline()
        self.manage_stages()

    def connect_signals(self):
        # Add buttons
        self.ui.btn_malt_add.clicked.connect(self.on_add_malt)
        self.ui.btn_hop_add.clicked.connect(self.on_add_hop)
        self.ui.btn_yeast_add.clicked.connect(self.on_add_yeast)
        self.ui.btn_summary_water_up.clicked.connect(self.on_water_add)

        # Reset button
        self.ui.btn_reset.clicked.connect(self.reset)

        # stage Buttons
        self.ui.btn_brewing_stage_next.clicked.connect(self.stage_next)
        self.ui.btn_brewing_stage_prev.clicked.connect(self.stage_prev)

        # Summary item selection
        self.ui.list_summary_malts.itemClicked.connect(self.on_malt_selected)
        self.ui.list_summary_hops.itemClicked.connect(self.on_hop_selected)
        self.ui.list_summary_yeast.itemClicked.connect(self.on_yeast_selected)

        # Search Edit
        self.ui.edit_malt_search.textChanged.connect(self.search_malt)
        self.ui.edit_hop_search.textChanged.connect(self.search_hop)
        self.ui.edit_yeast_search.textChanged.connect(self.search_yeast)

        # Sliders & inputs synchronization
        self.ui.slider_malt_weight.valueChanged.connect(
            lambda val: self.ui.edit_malt_weight.setText(f"{val / 10:.1f} kg")
        )
        self.ui.slider_hop_weight.valueChanged.connect(
            lambda val: self.ui.edit_hop_weight.setText(f"{val} g")
        )
        self.ui.slider_hop_time.valueChanged.connect(
            lambda val: self.ui.edit_hop_time.setText(f"{val} min")
        )


        # Temperature slider
        self.ui.slider_temperature.valueChanged.connect(
            lambda val: self.ui.lbl_temperature_value.setText(f"{val} ˚C")
        )

        # Timeline slider
        self.ui.slider_timeline.valueChanged.connect(self.refresh_timeline)

        # Timeline play/pause
        self.ui.btn_timeline_play_pause.clicked.connect(self.toggle_play)
        self.ui.btn_timeline_fast_forward.clicked.connect(self.set_fast_forward)
        self.ui.btn_timeline_rewind.clicked.connect(self.set_rewind)
        self.timeline_timer.timeout.connect(self.tick_timeline)

        # Stage metrics
        self.ui.slider_temperature.sliderReleased.connect(self.set_temp)
        self.ui.slider_timeline.valueChanged.connect(self.refresh_stage_metrics)
        self.ui.btn_timeline_stop_stage.clicked.connect(self.stop_stage)

    def reset(self):
        self.recipe.reset()
        self.mashing_end = 12000
        self.boiling_end = 12000
        self.fermenting_end = 3000
        self.current_stage = 0
        self.stage = 0
        self.ui.list_summary_malts.clear()
        self.ui.list_summary_hops.clear()
        self.ui.list_summary_yeast.clear()
        self.ui.edit_summary_water.setText("0.0 L")
        self.ui.slider_temperature.setValue(0)
        self.init_sim()
        self.refresh_metrics()

    def on_malt_selected(self, current):
        if not current:
            return

        malt = next((m for m in self.repo.get_malts() if m.name == " (".join(current.text().split(" (")[:-1])), None)
        if malt:
            self.ui.lbl_info_title.setText(malt.name)
            self.ui.lbl_info_description.setText(f"Origin: {malt.origin}\n"
                                                 f"SRM: {malt.color}\n"
                                                 f"PPG: {(malt.potential-1)*1000:.1f}")

    def on_hop_selected(self, current):
        if not current:
            return

        hop = next((h for h in self.repo.get_hops() if h.name == " (".join(current.text().split(" (")[:-1])), None)
        if hop:
            self.ui.lbl_info_title.setText(hop.name)
            self.ui.lbl_info_description.setText(f"Origin: {hop.origin}\n"
                                                 f"Type: {hop.type}\n"
                                                 f"Alpha: {hop.alpha}\n"
                                                 f"Beta: {hop.beta}")

    def on_yeast_selected(self, current):
        if not current:
            return

        yeast = next((y for y in self.repo.get_yeasts() if y.name == " (".join(current.text().split(" (")[:-1])), None)
        if yeast:
            self.ui.lbl_info_title.setText(yeast.name)
            self.ui.lbl_info_description.setText(f"Lab: {yeast.lab}\n"
                                                 f"Type: {yeast.type}\n"
                                                 f"Form: {yeast.form}\n"
                                                 f"Temp: {yeast.min_temp}˚C - {yeast.max_temp}˚C\n"
                                                 f"Attenuation: {yeast.attenuation}\n"
                                                 f"Flocculation: {yeast.flocculation}")

    def on_add_malt(self):
        row = self.ui.tbl_malts.currentRow()
        if row < 0:
            return

        name_item = self.ui.tbl_malts.item(row, 1)
        if not name_item:
            return

        weight = self.ui.slider_malt_weight.value() / 10.0
        malt = next((m for m in self.repo.get_malts() if m.name == name_item.text()), None)
        if malt:
            self.recipe.add_malt(malt, weight)
            self.ui.list_summary_malts.addItem(f"{malt.name} ({weight:.1f} kg)")
            self.refresh_metrics()
            self.update_simulation_vessels()
            self.info_help()

    def on_add_hop(self):
        row = self.ui.tbl_hops.currentRow()
        if row < 0:
            return

        name_item = self.ui.tbl_hops.item(row, 1)
        if not name_item:
            return

        weight = self.ui.slider_hop_weight.value()
        time = self.ui.slider_hop_time.value()
        hop = next((h for h in self.repo.get_hops() if h.name == name_item.text()), None)
        if hop:
            self.recipe.add_hop(hop, weight, time)
            self.ui.list_summary_hops.addItem(f"{hop.name} ({weight}g, {time}min)")
            self.refresh_metrics()
            self.boiling_end = max((h[2]*100 for h in self.recipe.hops), default=6000)
            self.set_up_timeline()
            self.update_simulation_vessels()
            self.info_help()

    def on_add_yeast(self):
        row = self.ui.tbl_yeasts.currentRow()
        if row < 0:
            return

        name_item = self.ui.tbl_yeasts.item(row, 0)
        if not name_item:
            return

        yeast = next((y for y in self.repo.get_yeasts() if y.name == name_item.text()), None)
        if yeast:
            self.recipe.add_yeast(yeast)
            self.ui.list_summary_yeast.clear()
            self.ui.list_summary_yeast.addItem(f"{yeast.name} ({yeast.lab})")
            self.refresh_metrics()
            self.update_simulation_vessels()
            self.info_help()

    def on_water_add(self):
        self.recipe.set_water(self.recipe.current_water + 1, self.stage)
        self.ui.edit_summary_water.setText(f"{self.recipe.current_water:.1f} L")
        if self.stage == 0:
            self.ui.lbl_mashing_water.setText(f"Water: {self.recipe.current_water:.1f}")
        elif self.stage == 1:
            self.ui.lbl_boiling_water.setText(f"Water: {self.recipe.current_water:.1f}")
            self.ui.lbl_boiling_og.setText(f"OG: {self.recipe.current_og:.3f}")
        self.refresh_metrics()
        self.update_simulation_vessels()
        self.info_help()

    def refresh_metrics(self):
        self.ui.lbl_metric_og_value.setText(f"{self.recipe.og:.3f}")
        self.ui.lbl_metric_fg_value.setText(f"{self.recipe.fg:.3f}")
        self.ui.lbl_metric_abv_value.setText(f"{self.recipe.abv:.1f}%")
        self.ui.lbl_metric_ibu_value.setText(f"{self.recipe.ibu:.0f}")
        self.ui.lbl_metric_srm_value.setText(f"SRM: {self.recipe.srm:.0f}")
        self.ui.lbl_metric_rgb_preview.setStyleSheet(f"background-color: {self.srm_to_hex(self.recipe.srm)};")
        water = self.recipe.current_water if self.stage < 2 else (self.recipe.boiling_water if self.recipe.boiling_water > 0 else self.recipe.current_water)
        self.ui.edit_summary_water.setText(f"{water:.1f} L")

    def search_malt(self, s):
        self.ui.tbl_malts.setCurrentItem(None)

        if not s:
            return

        matching_items = self.ui.tbl_malts.findItems(s, Qt.MatchContains)
        if matching_items:
            item = matching_items[0]
            self.ui.tbl_malts.setCurrentItem(item)

    def search_hop(self, s):
        self.ui.tbl_hops.setCurrentItem(None)

        if not s:
            return

        matching_items = self.ui.tbl_hops.findItems(s, Qt.MatchContains)
        if matching_items:
            item = matching_items[0]
            self.ui.tbl_hops.setCurrentItem(item)

    def search_yeast(self, s):
        self.ui.tbl_yeasts.setCurrentItem(None)

        if not s:
            return

        matching_items = self.ui.tbl_yeasts.findItems(s, Qt.MatchContains)
        if matching_items:
            item = matching_items[0]
            self.ui.tbl_yeasts.setCurrentItem(item)

    def srm_to_hex(self, srm):
        srm_colors = {
            0: "#64B4F5",
            1: "#FFE699", 2: "#FFD878", 3: "#FFCA5A", 4: "#FFBF42", 5: "#FBB123",
            6: "#F8A600", 7: "#F39C00", 8: "#EA8F00", 9: "#E58500", 10: "#DE7C00",
            11: "#D77200", 12: "#CF6900", 13: "#CB6200", 14: "#C35900", 15: "#BB5100",
            16: "#B54C00", 17: "#B04500", 18: "#A63E00", 19: "#A13700", 20: "#9B3200",
            21: "#952D00", 22: "#8E2900", 23: "#882300", 24: "#821E00", 25: "#7B1A00",
            26: "#771900", 27: "#701400", 28: "#6A0E00", 29: "#660D00", 30: "#5E0B00",
            31: "#5A0A02", 32: "#600903", 33: "#520907", 34: "#4C0505", 35: "#470606",
            36: "#440607", 37: "#3F0708", 38: "#3B0607", 39: "#3A070B", 40: "#36080A"
        }
        srm = max(0, min(40, int(round(srm))))
        return srm_colors[srm]

    def update_simulation_vessels(self):
        self.vessel_mashing.set_state(self.recipe.current_water, self.srm_to_hex(self.recipe.current_srm))
        self.vessel_boiling.set_state(self.recipe.current_water, self.srm_to_hex(self.recipe.srm))
        vol = self.recipe.boiling_water if self.recipe.boiling_water > 0 else self.recipe.current_water
        self.vessel_fermenting.set_state(vol, self.srm_to_hex(self.recipe.srm))

    def draw_simulation(self, painter, width, height, volume=None, max_volume=40.0, liquid_color=None):
        if volume is None:
            volume = self.recipe.current_water
        return draw_simulation(painter, width, height, volume, max_volume, liquid_color)

    def stage_next(self):
        self.manage_stages(self.stage + 1)
        self.info_help()

    def stage_prev(self):
        self.manage_stages(self.stage - 1)
        self.info_help()

    def stop_stage(self):
        if self.stage == 0:
            self.recipe.stop_mashing()
            self.mashing_end = max(1, self.ui.slider_timeline.value())
            self.current_stage = max(self.current_stage, 1)
        elif self.stage == 1:
            self.recipe.stop_boiling()
            self.boiling_end = max(1, self.ui.slider_timeline.value())
            self.current_stage = max(self.current_stage, 2)
        elif self.stage == 2:
            self.recipe.stop_fermenting()
            self.fermenting_end = max(1, self.ui.slider_timeline.value())
            self.current_stage = max(self.current_stage, 3)

        if self.is_playing:
            self.toggle_play()

        self.refresh_metrics()
        self.manage_stages(self.stage)
        self.info_stop_stage()

    def set_up_timeline(self):
        self.ui.slider_timeline.blockSignals(True)
        if self.stage == 0:
            self.ui.slider_timeline.setRange(0, self.mashing_end)
            if self.stage == self.current_stage:
                self.ui.slider_timeline.setValue(0)
                self.recipe.set_time(0.0)
            else:
                self.ui.slider_timeline.setValue(self.mashing_end)
                self.recipe.set_time(self.mashing_end / 100)
        elif self.stage == 1:
            self.ui.slider_timeline.setRange(0, self.boiling_end)
            if self.stage == self.current_stage:
                self.ui.slider_timeline.setValue(0)
                self.recipe.set_time(0.0)
            else:
                self.ui.slider_timeline.setValue(self.boiling_end)
                self.recipe.set_time(self.boiling_end / 100)
        elif self.stage == 2:
            self.ui.slider_timeline.setRange(0, self.fermenting_end)
            if self.stage == self.current_stage:
                self.ui.slider_timeline.setValue(0)
                self.recipe.set_time(0.0)
                if self.ui.slider_temperature.value() == 0 or self.ui.slider_temperature.value() == 100:
                    self.ui.slider_temperature.setValue(20)
                    self.set_temp()
            else:
                self.ui.slider_timeline.setValue(self.fermenting_end)
                self.recipe.set_time(self.fermenting_end / 100)
        self.ui.slider_timeline.blockSignals(False)
        self.refresh_stage_metrics(self.ui.slider_timeline.value())

    def refresh_timeline(self, val):
        if self.stage == 0:
            self.ui.lbl_timeline_time.setText(f"{int(val/100):02}:{int((val%100)*60/100):02}")
        elif self.stage == 1:
            self.ui.lbl_timeline_time.setText(f"{int(val/100):02}:{int((val%100)*60/100):02}")
        elif self.stage == 2:
            self.ui.lbl_timeline_time.setText(f"Day {int(val/100) }")

    def toggle_play(self):
        self.is_playing = not self.is_playing
        self.ui.btn_timeline_play_pause.setText("⏸" if self.is_playing else "▶")

        if self.is_playing:
            self.ui.slider_temperature.setEnabled(False)
            if self.playback_rate <= 0:
                self.playback_rate = 1
            self.timeline_timer.start(10)
        else:
            if self.stage == 0 or self.stage == 2:
                self.ui.slider_temperature.setEnabled(True)
            self.playback_rate = 0
            self.timeline_timer.stop()
        self.ui.lbl_timeline_speed.setText(f"{self.playback_rate}x")

    def set_fast_forward(self):
        if self.playback_rate > 0 and self.playback_rate < 16:
            self.playback_rate *= 2
        else:
            self.playback_rate = 2
        self.ui.lbl_timeline_speed.setText(f"{self.playback_rate}x")
        if not self.is_playing:
            self.toggle_play()

    def set_rewind(self):
        if self.playback_rate < 0 and self.playback_rate > -16:
            self.playback_rate *= 2
        else:
            self.playback_rate = -2
        self.ui.lbl_timeline_speed.setText(f"{self.playback_rate}x")
        if not self.is_playing:
            self.is_playing = True
            self.timeline_timer.start(10)
            self.ui.btn_timeline_play_pause.setText("⏸")

    def tick_timeline(self):
        current_val = self.ui.slider_timeline.value()
        max_val = self.ui.slider_timeline.maximum()
        base_step = 1
        new_val = current_val + (self.playback_rate * base_step)

        if new_val >= max_val:
            new_val = max_val
            if self.is_playing:
                self.toggle_play()
        elif new_val <= 0:
            new_val = 0
            if self.is_playing:
                self.toggle_play()

        self.ui.slider_timeline.setValue(new_val)

    def refresh_stage_metrics(self, time):
        self.recipe.set_time(time / 100)
        if self.stage == 0:
            self.recipe.update_mashing()
            self.ui.lbl_mashing_water.setText(f"Water: {self.recipe.current_water:.1f}")
            self.ui.lbl_mashing_og.setText(f"OG: {self.recipe.current_og:.3f}")
            self.ui.lbl_mashing_srm.setText(f"SRM: {round(self.recipe.current_srm)}")
            if self.recipe.temp > 0:
                self.ui.slider_temperature.setValue(int(round(self.recipe.temp)))
        elif self.stage == 1:
            self.recipe.update_boiling()
            self.ui.lbl_boiling_water.setText(f"Water: {self.recipe.current_water:.1f}")
            self.ui.lbl_boiling_og.setText(f"OG: {self.recipe.current_og:.3f}")
            self.ui.lbl_boiling_ibu.setText(f"IBU: {round(self.recipe.current_ibu)}")
            self.ui.edit_summary_water.setText(f"{self.recipe.current_water:.1f} L")
        elif self.stage == 2:
            self.recipe.update_fermenting()
            self.ui.lbl_fermenting_fg.setText(f"FG: {self.recipe.current_fg:.3f}")
            self.ui.lbl_fermenting_abv.setText(f"ABV: {self.recipe.current_abv:.1f}%")
            if self.recipe.temp > 0:
                self.ui.slider_temperature.setValue(int(round(self.recipe.temp)))
        self.update_simulation_vessels()

    def set_temp(self):
        self.recipe.set_temp(self.ui.slider_temperature.value(), self.stage)
        self.refresh_stage_metrics(self.ui.slider_timeline.value())
        self.info_help()

    def manage_stages(self, target_stage=None):
        if target_stage is not None:
            if target_stage <= self.current_stage:
                self.stage = max(0, min(int(target_stage), 2))
            else:
                self.stage = max(0, min(self.stage, self.current_stage, 2))
        else:
            self.stage = max(0, min(self.stage, self.current_stage, 2))

        # Update brewing stage title
        stage_names = {0: "Mashing", 1: "Boiling", 2: "Fermentation"}
        self.ui.lbl_brewing_stage_title.setText(stage_names.get(self.stage, "Mashing"))

        # Update visible stacked widgets
        self.ui.stacked_widget_stage.setCurrentIndex(self.stage)
        self.ui.tab_widget_ingredients.setCurrentIndex(self.stage)
        self.set_up_timeline()

        # Stage navigation buttons
        self.ui.btn_brewing_stage_prev.setEnabled(self.stage > 0)
        self.ui.btn_brewing_stage_next.setEnabled(self.stage < self.current_stage and self.stage < 2)

        # Check whether this stage is active
        is_active = (self.stage == self.current_stage)

        # Stage-stop controls
        self.ui.btn_timeline_stop_stage.setEnabled(is_active and self.current_stage <= 2)

        # Temperature control
        if self.stage == 0:
            self.ui.slider_temperature.setEnabled(is_active)
        elif self.stage == 1:
            self.ui.slider_temperature.setEnabled(False)
            self.ui.slider_temperature.setValue(100)
            self.set_temp()
        elif self.stage == 2:
            self.ui.slider_temperature.setEnabled(is_active)

        # Water volume controls
        can_edit_water = (self.stage in (0, 1) and is_active)
        self.ui.frame_summary_water.setEnabled(can_edit_water)
        self.ui.btn_summary_water_up.setEnabled(can_edit_water)

        # Stage 0
        can_add_malt = (self.stage == 0 and is_active)
        self.ui.tab_malts.setEnabled(can_add_malt)

        # Stage 1
        can_add_hop = (self.stage == 1 and is_active)
        self.ui.tab_hops.setEnabled(can_add_hop)

        # Stage 2
        can_add_yeast = (self.stage == 2 and is_active)
        self.ui.tab_yeasts.setEnabled(can_add_yeast)

        self.update_simulation_vessels()

    def info_help(self):
        if self.current_stage == self.stage == 0:
            if self.recipe.current_water <= 0:
                self.ui.lbl_info_title.setText("Add Water")
                self.ui.lbl_info_description.setText(
                    "Add water to set your initial mash water volume.\n"
                    "The recommended volume: 15-20 Liters")
            elif not self.recipe.malts:
                self.ui.lbl_info_title.setText("Add Malt Grains")
                self.ui.lbl_info_description.setText(
                    "Select a grain" + " from the malts tab, adjust the weight slider and add the malt.\n"
                    "The recommended weight: 4 kg of base malt for 20 Liters")
            elif self.ui.slider_temperature.value() <= 50 or self.ui.slider_temperature.value() >= 70:
                self.ui.lbl_info_title.setText("Set the Temperature")
                self.ui.lbl_info_description.setText(
                    "Move the temperature slider to your target mash temperature.\n"
                    "The recommended temperature: 62-71 ˚C\n"
                    "The optimal starch conversion peaks at 67 ˚C")
            else:
                self.ui.lbl_info_title.setText("Simulate the mashing stage")
                self.ui.lbl_info_description.setText(
                    "Press Play (▶) or scrub the Timeline slider forward.\n"
                    "Press Stop stage button to end the mashing.\n"
                    "The recommended time for mashing: 60-90 minutes")
        elif self.current_stage == self.stage == 1:
            if self.recipe.current_water <= 0:
                self.ui.lbl_info_title.setText("Add Water")
                self.ui.lbl_info_description.setText(
                    "Add water to set your initial mash water volume.\n"
                    "The recommended volume: 15-20 Liters")
            elif not self.recipe.hops:
                self.ui.lbl_info_title.setText("Add Hops")
                self.ui.lbl_info_description.setText(
                    "Select a hop" + " from the hops tab, adjust the weight and time slider and add the hop.\n"
                    "The recommended final IBU:\n"
                    "      • 5-40 for Lagers\n"
                    "      • 25-100+ for Ales")
            else:
                self.ui.lbl_info_title.setText("Simulate the boiling stage")
                self.ui.lbl_info_description.setText(
                    "Press Play (▶) or scrub the Timeline slider forward.\n"
                    "Press Stop stage button to end the boiling.\n"
                    "The recommended time for boiling: 60-90 minutes")
        elif self.current_stage == self.stage == 2:
            if not self.recipe.yeast:
                self.ui.lbl_info_title.setText("Add Yeast")
                self.ui.lbl_info_description.setText(
                    "Select a yeast" + " from the yeast tab and add it.")
            elif self.ui.slider_temperature.value() <= self.recipe.yeast.min_temp or self.ui.slider_temperature.value() >= self.recipe.yeast.max_temp:
                self.ui.lbl_info_title.setText("Set the Temperature")
                self.ui.lbl_info_description.setText(
                    "Move the temperature slider to your target fermentation temperature.\n"
                    f"The recommended temperature for {self.recipe.yeast.name}: {self.recipe.yeast.min_temp}˚C - {self.recipe.yeast.max_temp}˚C\n")
            else:
                self.ui.lbl_info_title.setText("Simulate the fermentation stage")
                self.ui.lbl_info_description.setText(
                    "Press Play (▶) or scrub the Timeline slider forward.\n"
                    "Press Stop stage button to end the fermentation.\n"
                    "The recommended time for fermentation: 14 days")
        else:
            self.info_stop_stage()

    def info_stop_stage(self):
        if self.stage == 0:
            self.ui.lbl_info_title.setText("Advance to the Next Stage")
            self.ui.lbl_info_description.setText(
                "Here are the results after mashing: \n"
                f"      • OG: {self.recipe.mashing_og:.3f}\n"
                f"      • SRM: {round(self.recipe.mashing_srm)}\n"
                f"      • Water: {self.recipe.mashing_water:.1f}")
        elif self.stage == 1:
            self.ui.lbl_info_title.setText("Advance to the Next Stage")
            self.ui.lbl_info_description.setText(
                "Here are the results after boiling: \n"
                f"      • OG: {self.recipe.boiling_og:.3f}\n"
                f"      • IBU: {self.recipe.boiling_ibu:.2f}\n"
                f"      • Water: {self.recipe.boiling_water:.1f}")
        elif self.stage == 2:
            self.ui.lbl_info_title.setText("End of Simulation and the Beer is Ready")
            self.ui.lbl_info_description.setText(
                "Here are the results after fermentation: \n"
                f"      • OG: {self.recipe.fermenting_fg:.3f}\n"
                f"      • ABV: {self.recipe.fermenting_abv}%")
