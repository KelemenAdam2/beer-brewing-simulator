# -*- coding: utf-8 -*-
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QAbstractItemView

try:
    from src.core.model import Malt, Hop, Yeast
except ModuleNotFoundError:
    from core.model import Malt, Hop, Yeast
from src.ui.pyside_ui.ui_form import Ui_MainWindow
from src.core.repository import Repository
from src.core.recipe import Recipe


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Core logic models
        self.repo = Repository()
        self.recipe = Recipe()

        # Timeline state
        self.is_playing = False

        # Wire up data and events
        self.init_data()
        self.connect_signals()

    def init_data(self):
        # 1. Populate Malts
        malts = self.repo.get_malts()
        self.ui.tbl_malts.clear()
        self.ui.tbl_malts.setColumnCount(4)
        self.ui.tbl_malts.setHorizontalHeaderLabels(["Name", "Origin", "Color", "Potential"])
        self.ui.tbl_malts.setRowCount(len(malts))
        self.ui.tbl_malts.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.ui.tbl_malts.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.ui.tbl_malts.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        for row, malt in enumerate(malts):
            self.ui.tbl_malts.setItem(row, 0, QTableWidgetItem(str(malt.name)))
            self.ui.tbl_malts.setItem(row, 1, QTableWidgetItem(str(malt.origin)))
            self.ui.tbl_malts.setItem(row, 2, QTableWidgetItem(str(malt.color)))
            self.ui.tbl_malts.setItem(row, 3, QTableWidgetItem(str(malt.potential)))

        # 2. Populate Hops
        hops = self.repo.get_hops()
        self.ui.tbl_hops.clear()
        self.ui.tbl_hops.setColumnCount(5)
        self.ui.tbl_hops.setHorizontalHeaderLabels(["Name", "Origin", "Type", "Alpha", "Beta"])
        self.ui.tbl_hops.setRowCount(len(hops))
        self.ui.tbl_hops.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.ui.tbl_hops.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.ui.tbl_hops.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        for row, hop in enumerate(hops):
            self.ui.tbl_hops.setItem(row, 0, QTableWidgetItem(str(hop.name)))
            self.ui.tbl_hops.setItem(row, 1, QTableWidgetItem(str(hop.origin)))
            self.ui.tbl_hops.setItem(row, 2, QTableWidgetItem(str(hop.type)))
            self.ui.tbl_hops.setItem(row, 3, QTableWidgetItem(str(hop.alpha)))
            self.ui.tbl_hops.setItem(row, 4, QTableWidgetItem(str(hop.beta)))

        # 3. Populate Yeasts
        yeasts = self.repo.get_yeasts()
        self.ui.tbl_yeasts.clear()
        self.ui.tbl_yeasts.setColumnCount(7)
        self.ui.tbl_yeasts.setHorizontalHeaderLabels(["Name", "Lab", "Form", "Type", "Temp", "Attenuation", "Flocculation"])
        self.ui.tbl_yeasts.setRowCount(len(yeasts))
        self.ui.tbl_yeasts.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.ui.tbl_yeasts.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.ui.tbl_yeasts.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
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
        self.recipe.batch_size = 0.0

        # Select first items if available
        if self.ui.tbl_malts.rowCount() > 0:
            self.ui.tbl_malts.selectRow(0)
        if self.ui.tbl_hops.rowCount() > 0:
            self.ui.tbl_hops.selectRow(0)
        if self.ui.tbl_yeasts.rowCount() > 0:
            self.ui.tbl_yeasts.selectRow(0)

        self.refresh_metrics()

    def connect_signals(self):
        # Add buttons
        self.ui.btn_malt_add.clicked.connect(self.on_add_malt)
        self.ui.btn_hop_add.clicked.connect(self.on_add_hop)
        self.ui.btn_yeast_add.clicked.connect(self.on_add_yeast)
        self.ui.btn_summary_water_up.clicked.connect(self.on_water_add)
        self.ui.btn_summary_water_down.clicked.connect(self.on_water_sub)

        # Reset button
        self.ui.btn_reset.clicked.connect(self.reset)

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
        self.ui.edit_summary_water.editingFinished.connect(self.on_water_edited)

        # Temperature slider
        self.ui.slider_temperature.valueChanged.connect(
            lambda val: self.ui.lbl_temperature_value.setText(f"{val} ˚C")
        )

        # Timeline play/pause
        self.ui.btn_timeline_play_pause.clicked.connect(self.toggle_play)

    def reset(self):
        self.recipe.reset()
        self.ui.list_summary_malts.clear()
        self.ui.list_summary_hops.clear()
        self.ui.list_summary_yeast.clear()
        self.update_water_edit()

    def on_malt_selected(self, current, _):
        if not current:
            return
        malt = next((m for m in self.repo.get_malts() if m.name == current.text()), None)
        if malt:
            self.ui.lbl_info_title.setText(malt.name)
            self.ui.lbl_info_description.setText(f"Origin: {malt.origin}"
                                                 f"SRM: {malt.color}"
                                                 f"PPG: {(malt.potential-1)*1000}")

    def on_hop_selected(self, current, _):
        if not current:
            return
        hop = next((h for h in self.repo.get_hops() if h.name == current.text()), None)
        if hop:
            self.ui.lbl_hop_origin_value.setText(hop.origin)
            self.ui.lbl_hop_type_value.setText(hop.type)
            self.ui.lbl_hop_alpha_value.setText(f"{hop.alpha}%")
            self.ui.lbl_hop_beta_value.setText(f"{hop.beta}%")

    def on_yeast_selected(self, current, _):
        if not current:
            return
        yeast = next((y for y in self.repo.get_yeasts() if y.name == current.text()), None)
        if yeast:
            self.ui.lbl_yeast_lab_value.setText(yeast.lab)
            self.ui.lbl_yeast_type_value.setText(yeast.type)
            self.ui.lbl_yeast_form_value.setText(yeast.form)
            self.ui.lbl_yeast_temp_value.setText(f"{yeast.min_temp} °C - {yeast.max_temp} °C")
            self.ui.lbl_yeast_attenuation_value.setText(f"{int(yeast.attenuation * 100)}%")
            self.ui.lbl_yeast_flocculation_value.setText(yeast.flocculation)

    def on_add_malt(self):
        item = self.ui.tbl_malts.currentItem()
        if not item:
            return
        weight = self.ui.slider_malt_weight.value() / 10.0
        malt = next((m for m in self.repo.get_malts() if m.name == item.text()), None)
        if malt:
            self.recipe.add_malt(malt, weight)
            self.ui.list_summary_malts.addItem(f"{malt.name} ({weight:.1f} kg)")
            self.refresh_metrics()

    def on_add_hop(self):
        item = self.ui.tbl_hops.currentItem()
        if not item:
            return
        weight = self.ui.slider_hop_weight.value()
        time = self.ui.slider_hop_time.value()
        hop = next((h for h in self.repo.get_hops() if h.name == item.text()), None)
        if hop:
            self.recipe.add_hop(hop, weight, time)
            self.ui.list_summary_hops.addItem(f"{hop.name} ({weight}g, {time}min)")
            self.refresh_metrics()

    def on_add_yeast(self):
        item = self.ui.tbl_yeasts.currentItem()
        if not item:
            return
        yeast = next((y for y in self.repo.get_yeasts() if y.name == item.text()), None)
        if yeast:
            self.recipe.remove_yeast()
            self.recipe.add_yeast(yeast)
            self.ui.list_summary_yeast.clear()
            self.ui.list_summary_yeast.addItem(f"{yeast.name} ({yeast.lab})")
            self.refresh_metrics()

    def on_water_add(self):
        self.recipe.add_water(1)
        self.update_water_edit()

    def on_water_sub(self):
        self.recipe.add_water(-1)
        self.update_water_edit()

    def update_water_edit(self):
        self.ui.edit_summary_water.setText(str(self.recipe.batch_size) + " L")
        self.refresh_metrics()

    def on_water_edited(self):
        text = self.ui.edit_summary_water.text().replace("L", "").strip()
        try:
            vol = float(text)
            self.recipe.set_water(vol)
            self.refresh_metrics()
        except ValueError:
            pass

    def refresh_metrics(self):
        self.ui.lbl_metric_og_value.setText(f"{self.recipe.og:.3f}")
        self.ui.lbl_metric_fg_value.setText(f"{self.recipe.fg:.3f}")
        self.ui.lbl_metric_abv_value.setText(f"{self.recipe.abv:.1f}%")
        self.ui.lbl_metric_ibu_value.setText(f"{self.recipe.ibu:.0f}")
        self.ui.lbl_metric_srm_value.setText(f"SRM: {self.recipe.srm:.0f}")

    def toggle_play(self):
        self.is_playing = not self.is_playing
        self.ui.btn_timeline_play_pause.setText("⏸" if self.is_playing else "▶")