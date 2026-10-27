# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formMxXDqt.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(1024, 640))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layout_main = QHBoxLayout(self.centralwidget)
        self.layout_main.setSpacing(8)
        self.layout_main.setObjectName(u"layout_main")
        self.layout_main.setContentsMargins(8, 8, 8, 8)
        self.layout_left_column = QVBoxLayout()
        self.layout_left_column.setSpacing(8)
        self.layout_left_column.setObjectName(u"layout_left_column")
        self.layout_state_and_temp = QHBoxLayout()
        self.layout_state_and_temp.setSpacing(8)
        self.layout_state_and_temp.setObjectName(u"layout_state_and_temp")
        self.frame_brewing_state = QFrame(self.centralwidget)
        self.frame_brewing_state.setObjectName(u"frame_brewing_state")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_brewing_state.sizePolicy().hasHeightForWidth())
        self.frame_brewing_state.setSizePolicy(sizePolicy)
        self.frame_brewing_state.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_brewing_state.setFrameShadow(QFrame.Shadow.Raised)
        self.layout_brewing_state = QVBoxLayout(self.frame_brewing_state)
        self.layout_brewing_state.setObjectName(u"layout_brewing_state")
        self.layout_state_and_button = QHBoxLayout()
        self.layout_state_and_button.setObjectName(u"layout_state_and_button")
        self.lbl_brewing_state_title = QLabel(self.frame_brewing_state)
        self.lbl_brewing_state_title.setObjectName(u"lbl_brewing_state_title")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbl_brewing_state_title.sizePolicy().hasHeightForWidth())
        self.lbl_brewing_state_title.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.lbl_brewing_state_title.setFont(font)
        self.lbl_brewing_state_title.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.layout_state_and_button.addWidget(self.lbl_brewing_state_title)

        self.btn_reset = QPushButton(self.frame_brewing_state)
        self.btn_reset.setObjectName(u"btn_reset")
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.btn_reset.setFont(font1)

        self.layout_state_and_button.addWidget(self.btn_reset)

        self.layout_state_and_button.setStretch(0, 10)
        self.layout_state_and_button.setStretch(1, 1)

        self.layout_brewing_state.addLayout(self.layout_state_and_button)

        self.layout_brewing_state_controls = QHBoxLayout()
        self.layout_brewing_state_controls.setObjectName(u"layout_brewing_state_controls")
        self.layout_brewing_state_controls.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.btn_brewing_state_prev = QPushButton(self.frame_brewing_state)
        self.btn_brewing_state_prev.setObjectName(u"btn_brewing_state_prev")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_brewing_state_prev.sizePolicy().hasHeightForWidth())
        self.btn_brewing_state_prev.setSizePolicy(sizePolicy2)
        self.btn_brewing_state_prev.setMinimumSize(QSize(42, 70))
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        self.btn_brewing_state_prev.setFont(font2)
        self.btn_brewing_state_prev.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.layout_brewing_state_controls.addWidget(self.btn_brewing_state_prev)

        self.widget_brewing_state_display = QWidget(self.frame_brewing_state)
        self.widget_brewing_state_display.setObjectName(u"widget_brewing_state_display")
        self.layout_brewing_state_display = QVBoxLayout(self.widget_brewing_state_display)
        self.layout_brewing_state_display.setObjectName(u"layout_brewing_state_display")
        self.spacer_placeholder = QSpacerItem(20, 200, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.layout_brewing_state_display.addItem(self.spacer_placeholder)


        self.layout_brewing_state_controls.addWidget(self.widget_brewing_state_display)

        self.btn_brewing_state_next = QPushButton(self.frame_brewing_state)
        self.btn_brewing_state_next.setObjectName(u"btn_brewing_state_next")
        sizePolicy2.setHeightForWidth(self.btn_brewing_state_next.sizePolicy().hasHeightForWidth())
        self.btn_brewing_state_next.setSizePolicy(sizePolicy2)
        self.btn_brewing_state_next.setMinimumSize(QSize(42, 70))
        self.btn_brewing_state_next.setFont(font2)
        self.btn_brewing_state_next.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.layout_brewing_state_controls.addWidget(self.btn_brewing_state_next)

        self.layout_brewing_state_controls.setStretch(0, 1)
        self.layout_brewing_state_controls.setStretch(1, 20)
        self.layout_brewing_state_controls.setStretch(2, 1)

        self.layout_brewing_state.addLayout(self.layout_brewing_state_controls)

        self.layout_brewing_state.setStretch(1, 8)

        self.layout_state_and_temp.addWidget(self.frame_brewing_state)

        self.frame_temperature = QFrame(self.centralwidget)
        self.frame_temperature.setObjectName(u"frame_temperature")
        self.frame_temperature.setMinimumSize(QSize(75, 0))
        self.frame_temperature.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_temperature.setFrameShadow(QFrame.Shadow.Raised)
        self.layout_temperature = QVBoxLayout(self.frame_temperature)
        self.layout_temperature.setSpacing(6)
        self.layout_temperature.setObjectName(u"layout_temperature")
        self.lbl_temperature_header = QLabel(self.frame_temperature)
        self.lbl_temperature_header.setObjectName(u"lbl_temperature_header")
        sizePolicy1.setHeightForWidth(self.lbl_temperature_header.sizePolicy().hasHeightForWidth())
        self.lbl_temperature_header.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setPointSize(13)
        font3.setBold(True)
        self.lbl_temperature_header.setFont(font3)
        self.lbl_temperature_header.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_temperature.addWidget(self.lbl_temperature_header)

        self.slider_temperature = QSlider(self.frame_temperature)
        self.slider_temperature.setObjectName(u"slider_temperature")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.slider_temperature.sizePolicy().hasHeightForWidth())
        self.slider_temperature.setSizePolicy(sizePolicy3)
        self.slider_temperature.setMaximum(100)
        self.slider_temperature.setValue(100)
        self.slider_temperature.setTracking(True)
        self.slider_temperature.setOrientation(Qt.Orientation.Vertical)
        self.slider_temperature.setInvertedControls(False)

        self.layout_temperature.addWidget(self.slider_temperature)

        self.lbl_temperature_value = QLabel(self.frame_temperature)
        self.lbl_temperature_value.setObjectName(u"lbl_temperature_value")
        sizePolicy1.setHeightForWidth(self.lbl_temperature_value.sizePolicy().hasHeightForWidth())
        self.lbl_temperature_value.setSizePolicy(sizePolicy1)
        self.lbl_temperature_value.setMinimumSize(QSize(68, 28))
        self.lbl_temperature_value.setFont(font1)
        self.lbl_temperature_value.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_temperature.addWidget(self.lbl_temperature_value)


        self.layout_state_and_temp.addWidget(self.frame_temperature)

        self.layout_state_and_temp.setStretch(0, 10)
        self.layout_state_and_temp.setStretch(1, 1)

        self.layout_left_column.addLayout(self.layout_state_and_temp)

        self.frame_timeline = QFrame(self.centralwidget)
        self.frame_timeline.setObjectName(u"frame_timeline")
        self.frame_timeline.setMinimumSize(QSize(0, 48))
        self.frame_timeline.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_timeline.setFrameShadow(QFrame.Shadow.Raised)
        self.layout_timeline = QHBoxLayout(self.frame_timeline)
        self.layout_timeline.setSpacing(8)
        self.layout_timeline.setObjectName(u"layout_timeline")
        self.btn_timeline_rewind = QPushButton(self.frame_timeline)
        self.btn_timeline_rewind.setObjectName(u"btn_timeline_rewind")
        self.btn_timeline_rewind.setMinimumSize(QSize(44, 34))
        self.btn_timeline_rewind.setFont(font2)
        self.btn_timeline_rewind.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.layout_timeline.addWidget(self.btn_timeline_rewind)

        self.btn_timeline_play_pause = QPushButton(self.frame_timeline)
        self.btn_timeline_play_pause.setObjectName(u"btn_timeline_play_pause")
        self.btn_timeline_play_pause.setMinimumSize(QSize(48, 34))
        self.btn_timeline_play_pause.setFont(font2)
        self.btn_timeline_play_pause.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.layout_timeline.addWidget(self.btn_timeline_play_pause)

        self.btn_timeline_fast_forward = QPushButton(self.frame_timeline)
        self.btn_timeline_fast_forward.setObjectName(u"btn_timeline_fast_forward")
        self.btn_timeline_fast_forward.setMinimumSize(QSize(44, 34))
        self.btn_timeline_fast_forward.setFont(font2)
        self.btn_timeline_fast_forward.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.layout_timeline.addWidget(self.btn_timeline_fast_forward)

        self.slider_timeline = QSlider(self.frame_timeline)
        self.slider_timeline.setObjectName(u"slider_timeline")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.slider_timeline.sizePolicy().hasHeightForWidth())
        self.slider_timeline.setSizePolicy(sizePolicy4)
        self.slider_timeline.setOrientation(Qt.Orientation.Horizontal)
        self.slider_timeline.setTickPosition(QSlider.TickPosition.NoTicks)
        self.slider_timeline.setTickInterval(0)

        self.layout_timeline.addWidget(self.slider_timeline)

        self.lbl_timeline_time = QLabel(self.frame_timeline)
        self.lbl_timeline_time.setObjectName(u"lbl_timeline_time")
        self.lbl_timeline_time.setMinimumSize(QSize(70, 30))
        self.lbl_timeline_time.setFont(font1)
        self.lbl_timeline_time.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.layout_timeline.addWidget(self.lbl_timeline_time)


        self.layout_left_column.addWidget(self.frame_timeline)

        self.layout_charts = QHBoxLayout()
        self.layout_charts.setSpacing(8)
        self.layout_charts.setObjectName(u"layout_charts")
        self.frame_recipe_summary = QFrame(self.centralwidget)
        self.frame_recipe_summary.setObjectName(u"frame_recipe_summary")
        sizePolicy.setHeightForWidth(self.frame_recipe_summary.sizePolicy().hasHeightForWidth())
        self.frame_recipe_summary.setSizePolicy(sizePolicy)
        self.frame_recipe_summary.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_recipe_summary.setFrameShadow(QFrame.Shadow.Raised)
        self.layout_recipe_summary_grid = QGridLayout(self.frame_recipe_summary)
        self.layout_recipe_summary_grid.setSpacing(6)
        self.layout_recipe_summary_grid.setObjectName(u"layout_recipe_summary_grid")
        self.layout_recipe_summary_grid.setContentsMargins(4, 4, 4, 4)
        self.frame_summary_malts = QFrame(self.frame_recipe_summary)
        self.frame_summary_malts.setObjectName(u"frame_summary_malts")
        self.frame_summary_malts.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_summary_malts.setFrameShadow(QFrame.Shadow.Raised)
        self.layout_summary_malts = QVBoxLayout(self.frame_summary_malts)
        self.layout_summary_malts.setSpacing(4)
        self.layout_summary_malts.setObjectName(u"layout_summary_malts")
        self.lbl_summary_malts_title = QLabel(self.frame_summary_malts)
        self.lbl_summary_malts_title.setObjectName(u"lbl_summary_malts_title")
        font4 = QFont()
        font4.setPointSize(18)
        font4.setBold(True)
        self.lbl_summary_malts_title.setFont(font4)
        self.lbl_summary_malts_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_summary_malts.addWidget(self.lbl_summary_malts_title)

        self.list_summary_malts = QListWidget(self.frame_summary_malts)
        self.list_summary_malts.setObjectName(u"list_summary_malts")
        font5 = QFont()
        font5.setPointSize(12)
        self.list_summary_malts.setFont(font5)

        self.layout_summary_malts.addWidget(self.list_summary_malts)


        self.layout_recipe_summary_grid.addWidget(self.frame_summary_malts, 0, 0, 1, 1)

        self.frame_summary_hops = QFrame(self.frame_recipe_summary)
        self.frame_summary_hops.setObjectName(u"frame_summary_hops")
        self.frame_summary_hops.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_summary_hops.setFrameShadow(QFrame.Shadow.Raised)
        self.layout_summary_hops = QVBoxLayout(self.frame_summary_hops)
        self.layout_summary_hops.setSpacing(4)
        self.layout_summary_hops.setObjectName(u"layout_summary_hops")
        self.lbl_summary_hops_title = QLabel(self.frame_summary_hops)
        self.lbl_summary_hops_title.setObjectName(u"lbl_summary_hops_title")
        self.lbl_summary_hops_title.setFont(font4)
        self.lbl_summary_hops_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_summary_hops.addWidget(self.lbl_summary_hops_title)

        self.list_summary_hops = QListWidget(self.frame_summary_hops)
        self.list_summary_hops.setObjectName(u"list_summary_hops")
        self.list_summary_hops.setFont(font5)

        self.layout_summary_hops.addWidget(self.list_summary_hops)


        self.layout_recipe_summary_grid.addWidget(self.frame_summary_hops, 0, 1, 1, 1)

        self.frame_summary_yeast = QFrame(self.frame_recipe_summary)
        self.frame_summary_yeast.setObjectName(u"frame_summary_yeast")
        self.frame_summary_yeast.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_summary_yeast.setFrameShadow(QFrame.Shadow.Raised)
        self.layout_summary_yeast = QVBoxLayout(self.frame_summary_yeast)
        self.layout_summary_yeast.setSpacing(4)
        self.layout_summary_yeast.setObjectName(u"layout_summary_yeast")
        self.lbl_summary_yeast_title = QLabel(self.frame_summary_yeast)
        self.lbl_summary_yeast_title.setObjectName(u"lbl_summary_yeast_title")
        self.lbl_summary_yeast_title.setFont(font4)
        self.lbl_summary_yeast_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_summary_yeast.addWidget(self.lbl_summary_yeast_title)

        self.list_summary_yeast = QListWidget(self.frame_summary_yeast)
        self.list_summary_yeast.setObjectName(u"list_summary_yeast")
        self.list_summary_yeast.setFont(font5)

        self.layout_summary_yeast.addWidget(self.list_summary_yeast)


        self.layout_recipe_summary_grid.addWidget(self.frame_summary_yeast, 1, 0, 1, 1)

        self.frame_summary_water = QFrame(self.frame_recipe_summary)
        self.frame_summary_water.setObjectName(u"frame_summary_water")
        self.frame_summary_water.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_summary_water.setFrameShadow(QFrame.Shadow.Raised)
        self.layout_summary_water = QVBoxLayout(self.frame_summary_water)
        self.layout_summary_water.setSpacing(4)
        self.layout_summary_water.setObjectName(u"layout_summary_water")
        self.lbl_summary_water_title = QLabel(self.frame_summary_water)
        self.lbl_summary_water_title.setObjectName(u"lbl_summary_water_title")
        self.lbl_summary_water_title.setFont(font4)
        self.lbl_summary_water_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_summary_water.addWidget(self.lbl_summary_water_title)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.layout_summary_water.addItem(self.verticalSpacer)

        self.edit_summary_water = QLineEdit(self.frame_summary_water)
        self.edit_summary_water.setObjectName(u"edit_summary_water")
        self.edit_summary_water.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.edit_summary_water.sizePolicy().hasHeightForWidth())
        self.edit_summary_water.setSizePolicy(sizePolicy4)
        self.edit_summary_water.setMinimumSize(QSize(0, 32))
        self.edit_summary_water.setFont(font4)
        self.edit_summary_water.setAutoFillBackground(False)
        self.edit_summary_water.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_summary_water.addWidget(self.edit_summary_water)

        self.layout_summary_water_buttons = QHBoxLayout()
        self.layout_summary_water_buttons.setObjectName(u"layout_summary_water_buttons")
        self.btn_summary_water_down = QPushButton(self.frame_summary_water)
        self.btn_summary_water_down.setObjectName(u"btn_summary_water_down")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.btn_summary_water_down.sizePolicy().hasHeightForWidth())
        self.btn_summary_water_down.setSizePolicy(sizePolicy5)
        self.btn_summary_water_down.setFont(font2)

        self.layout_summary_water_buttons.addWidget(self.btn_summary_water_down)

        self.btn_summary_water_up = QPushButton(self.frame_summary_water)
        self.btn_summary_water_up.setObjectName(u"btn_summary_water_up")
        sizePolicy5.setHeightForWidth(self.btn_summary_water_up.sizePolicy().hasHeightForWidth())
        self.btn_summary_water_up.setSizePolicy(sizePolicy5)
        self.btn_summary_water_up.setFont(font2)

        self.layout_summary_water_buttons.addWidget(self.btn_summary_water_up)

        self.layout_summary_water_buttons.setStretch(0, 1)
        self.layout_summary_water_buttons.setStretch(1, 1)

        self.layout_summary_water.addLayout(self.layout_summary_water_buttons)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.layout_summary_water.addItem(self.verticalSpacer_2)

        self.layout_summary_water.setStretch(0, 2)
        self.layout_summary_water.setStretch(1, 2)
        self.layout_summary_water.setStretch(2, 2)
        self.layout_summary_water.setStretch(3, 2)
        self.layout_summary_water.setStretch(4, 2)

        self.layout_recipe_summary_grid.addWidget(self.frame_summary_water, 1, 1, 1, 1)


        self.layout_charts.addWidget(self.frame_recipe_summary)

        self.frame_metrics = QFrame(self.centralwidget)
        self.frame_metrics.setObjectName(u"frame_metrics")
        sizePolicy.setHeightForWidth(self.frame_metrics.sizePolicy().hasHeightForWidth())
        self.frame_metrics.setSizePolicy(sizePolicy)
        self.frame_metrics.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_metrics.setFrameShadow(QFrame.Shadow.Raised)
        self.layout_metrics_grid = QGridLayout(self.frame_metrics)
        self.layout_metrics_grid.setSpacing(6)
        self.layout_metrics_grid.setObjectName(u"layout_metrics_grid")
        self.layout_metrics_grid.setContentsMargins(4, 4, 4, 4)
        self.frame_metric_gravity = QFrame(self.frame_metrics)
        self.frame_metric_gravity.setObjectName(u"frame_metric_gravity")
        self.frame_metric_gravity.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_metric_gravity.setFrameShadow(QFrame.Shadow.Raised)
        self.layout_metric_gravity = QHBoxLayout(self.frame_metric_gravity)
        self.layout_metric_gravity.setSpacing(4)
        self.layout_metric_gravity.setObjectName(u"layout_metric_gravity")
        self.layout_metric_og = QVBoxLayout()
        self.layout_metric_og.setObjectName(u"layout_metric_og")
        self.lbl_metric_og_title = QLabel(self.frame_metric_gravity)
        self.lbl_metric_og_title.setObjectName(u"lbl_metric_og_title")
        self.lbl_metric_og_title.setFont(font4)
        self.lbl_metric_og_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_metric_og.addWidget(self.lbl_metric_og_title)

        self.lbl_metric_og_value = QLabel(self.frame_metric_gravity)
        self.lbl_metric_og_value.setObjectName(u"lbl_metric_og_value")
        self.lbl_metric_og_value.setFont(font4)
        self.lbl_metric_og_value.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_metric_og.addWidget(self.lbl_metric_og_value)


        self.layout_metric_gravity.addLayout(self.layout_metric_og)

        self.layout_metric_fg = QVBoxLayout()
        self.layout_metric_fg.setObjectName(u"layout_metric_fg")
        self.lbl_metric_fg_title = QLabel(self.frame_metric_gravity)
        self.lbl_metric_fg_title.setObjectName(u"lbl_metric_fg_title")
        self.lbl_metric_fg_title.setFont(font4)
        self.lbl_metric_fg_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_metric_fg.addWidget(self.lbl_metric_fg_title)

        self.lbl_metric_fg_value = QLabel(self.frame_metric_gravity)
        self.lbl_metric_fg_value.setObjectName(u"lbl_metric_fg_value")
        self.lbl_metric_fg_value.setFont(font4)
        self.lbl_metric_fg_value.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_metric_fg.addWidget(self.lbl_metric_fg_value)


        self.layout_metric_gravity.addLayout(self.layout_metric_fg)


        self.layout_metrics_grid.addWidget(self.frame_metric_gravity, 0, 0, 1, 1)

        self.frame_metric_color = QFrame(self.frame_metrics)
        self.frame_metric_color.setObjectName(u"frame_metric_color")
        self.frame_metric_color.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_metric_color.setFrameShadow(QFrame.Shadow.Raised)
        self.layout_metric_color = QVBoxLayout(self.frame_metric_color)
        self.layout_metric_color.setSpacing(4)
        self.layout_metric_color.setObjectName(u"layout_metric_color")
        self.lbl_metric_color_title = QLabel(self.frame_metric_color)
        self.lbl_metric_color_title.setObjectName(u"lbl_metric_color_title")
        self.lbl_metric_color_title.setFont(font4)
        self.lbl_metric_color_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_metric_color.addWidget(self.lbl_metric_color_title)

        self.layout_metric_color_row = QHBoxLayout()
        self.layout_metric_color_row.setObjectName(u"layout_metric_color_row")
        self.lbl_metric_srm_value = QLabel(self.frame_metric_color)
        self.lbl_metric_srm_value.setObjectName(u"lbl_metric_srm_value")
        self.lbl_metric_srm_value.setFont(font4)
        self.lbl_metric_srm_value.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_metric_color_row.addWidget(self.lbl_metric_srm_value)

        self.lbl_metric_rgb_preview = QLabel(self.frame_metric_color)
        self.lbl_metric_rgb_preview.setObjectName(u"lbl_metric_rgb_preview")
        self.lbl_metric_rgb_preview.setFont(font4)
        self.lbl_metric_rgb_preview.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_metric_color_row.addWidget(self.lbl_metric_rgb_preview)


        self.layout_metric_color.addLayout(self.layout_metric_color_row)


        self.layout_metrics_grid.addWidget(self.frame_metric_color, 0, 1, 1, 1)

        self.frame_metric_abv = QFrame(self.frame_metrics)
        self.frame_metric_abv.setObjectName(u"frame_metric_abv")
        self.frame_metric_abv.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_metric_abv.setFrameShadow(QFrame.Shadow.Raised)
        self.layout_metric_abv = QVBoxLayout(self.frame_metric_abv)
        self.layout_metric_abv.setSpacing(4)
        self.layout_metric_abv.setObjectName(u"layout_metric_abv")
        self.lbl_metric_abv_title = QLabel(self.frame_metric_abv)
        self.lbl_metric_abv_title.setObjectName(u"lbl_metric_abv_title")
        self.lbl_metric_abv_title.setFont(font4)
        self.lbl_metric_abv_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_metric_abv.addWidget(self.lbl_metric_abv_title)

        self.lbl_metric_abv_value = QLabel(self.frame_metric_abv)
        self.lbl_metric_abv_value.setObjectName(u"lbl_metric_abv_value")
        self.lbl_metric_abv_value.setFont(font4)
        self.lbl_metric_abv_value.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_metric_abv.addWidget(self.lbl_metric_abv_value)


        self.layout_metrics_grid.addWidget(self.frame_metric_abv, 1, 0, 1, 1)

        self.frame_metric_ibu = QFrame(self.frame_metrics)
        self.frame_metric_ibu.setObjectName(u"frame_metric_ibu")
        self.frame_metric_ibu.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_metric_ibu.setFrameShadow(QFrame.Shadow.Raised)
        self.layout_metric_ibu = QVBoxLayout(self.frame_metric_ibu)
        self.layout_metric_ibu.setSpacing(4)
        self.layout_metric_ibu.setObjectName(u"layout_metric_ibu")
        self.lbl_metric_ibu_title = QLabel(self.frame_metric_ibu)
        self.lbl_metric_ibu_title.setObjectName(u"lbl_metric_ibu_title")
        self.lbl_metric_ibu_title.setFont(font4)
        self.lbl_metric_ibu_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_metric_ibu.addWidget(self.lbl_metric_ibu_title)

        self.lbl_metric_ibu_value = QLabel(self.frame_metric_ibu)
        self.lbl_metric_ibu_value.setObjectName(u"lbl_metric_ibu_value")
        self.lbl_metric_ibu_value.setFont(font4)
        self.lbl_metric_ibu_value.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_metric_ibu.addWidget(self.lbl_metric_ibu_value)


        self.layout_metrics_grid.addWidget(self.frame_metric_ibu, 1, 1, 1, 1)


        self.layout_charts.addWidget(self.frame_metrics)

        self.layout_charts.setStretch(0, 2)
        self.layout_charts.setStretch(1, 1)

        self.layout_left_column.addLayout(self.layout_charts)

        self.layout_left_column.setStretch(0, 8)
        self.layout_left_column.setStretch(1, 1)
        self.layout_left_column.setStretch(2, 8)

        self.layout_main.addLayout(self.layout_left_column)

        self.layout_right_column = QVBoxLayout()
        self.layout_right_column.setSpacing(8)
        self.layout_right_column.setObjectName(u"layout_right_column")
        self.frame_recipe_info = QFrame(self.centralwidget)
        self.frame_recipe_info.setObjectName(u"frame_recipe_info")
        self.frame_recipe_info.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_recipe_info.setFrameShadow(QFrame.Shadow.Raised)
        self.layout_recipe_info = QVBoxLayout(self.frame_recipe_info)
        self.layout_recipe_info.setSpacing(6)
        self.layout_recipe_info.setObjectName(u"layout_recipe_info")
        self.lbl_info_title = QLabel(self.frame_recipe_info)
        self.lbl_info_title.setObjectName(u"lbl_info_title")
        sizePolicy1.setHeightForWidth(self.lbl_info_title.sizePolicy().hasHeightForWidth())
        self.lbl_info_title.setSizePolicy(sizePolicy1)
        font6 = QFont()
        font6.setPointSize(22)
        font6.setBold(True)
        self.lbl_info_title.setFont(font6)
        self.lbl_info_title.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.layout_recipe_info.addWidget(self.lbl_info_title)

        self.lbl_info_description = QLabel(self.frame_recipe_info)
        self.lbl_info_description.setObjectName(u"lbl_info_description")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.lbl_info_description.sizePolicy().hasHeightForWidth())
        self.lbl_info_description.setSizePolicy(sizePolicy6)
        font7 = QFont()
        font7.setPointSize(13)
        self.lbl_info_description.setFont(font7)
        self.lbl_info_description.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.lbl_info_description.setWordWrap(True)

        self.layout_recipe_info.addWidget(self.lbl_info_description)

        self.layout_recipe_info.setStretch(0, 1)
        self.layout_recipe_info.setStretch(1, 5)

        self.layout_right_column.addWidget(self.frame_recipe_info)

        self.frame_ingredients = QFrame(self.centralwidget)
        self.frame_ingredients.setObjectName(u"frame_ingredients")
        self.frame_ingredients.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_ingredients.setFrameShadow(QFrame.Shadow.Raised)
        self.layout_ingredients = QVBoxLayout(self.frame_ingredients)
        self.layout_ingredients.setObjectName(u"layout_ingredients")
        self.layout_ingredients.setContentsMargins(6, 6, 6, 6)
        self.tab_widget_ingredients = QTabWidget(self.frame_ingredients)
        self.tab_widget_ingredients.setObjectName(u"tab_widget_ingredients")
        font8 = QFont()
        font8.setPointSize(14)
        font8.setBold(True)
        self.tab_widget_ingredients.setFont(font8)
        self.tab_widget_ingredients.setTabShape(QTabWidget.TabShape.Rounded)
        self.tab_widget_ingredients.setElideMode(Qt.TextElideMode.ElideRight)
        self.tab_widget_ingredients.setTabBarAutoHide(False)
        self.tab_malts = QWidget()
        self.tab_malts.setObjectName(u"tab_malts")
        self.layout_malts_tab = QVBoxLayout(self.tab_malts)
        self.layout_malts_tab.setSpacing(6)
        self.layout_malts_tab.setObjectName(u"layout_malts_tab")
        self.tbl_malts = QTableWidget(self.tab_malts)
        self.tbl_malts.setObjectName(u"tbl_malts")
        self.tbl_malts.setMinimumSize(QSize(0, 120))
        font9 = QFont()
        font9.setPointSize(12)
        font9.setBold(True)
        self.tbl_malts.setFont(font9)

        self.layout_malts_tab.addWidget(self.tbl_malts)

        self.layout_malt_weight = QHBoxLayout()
        self.layout_malt_weight.setObjectName(u"layout_malt_weight")
        self.lbl_malt_weight = QLabel(self.tab_malts)
        self.lbl_malt_weight.setObjectName(u"lbl_malt_weight")
        self.lbl_malt_weight.setMinimumSize(QSize(65, 30))
        self.lbl_malt_weight.setMaximumSize(QSize(65, 30))
        self.lbl_malt_weight.setFont(font3)
        self.lbl_malt_weight.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.layout_malt_weight.addWidget(self.lbl_malt_weight)

        self.slider_malt_weight = QSlider(self.tab_malts)
        self.slider_malt_weight.setObjectName(u"slider_malt_weight")
        sizePolicy4.setHeightForWidth(self.slider_malt_weight.sizePolicy().hasHeightForWidth())
        self.slider_malt_weight.setSizePolicy(sizePolicy4)
        self.slider_malt_weight.setOrientation(Qt.Orientation.Horizontal)

        self.layout_malt_weight.addWidget(self.slider_malt_weight)

        self.edit_malt_weight = QLineEdit(self.tab_malts)
        self.edit_malt_weight.setObjectName(u"edit_malt_weight")
        self.edit_malt_weight.setMinimumSize(QSize(75, 30))
        self.edit_malt_weight.setMaximumSize(QSize(85, 30))
        self.edit_malt_weight.setFont(font3)
        self.edit_malt_weight.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.layout_malt_weight.addWidget(self.edit_malt_weight)

        self.layout_malt_weight.setStretch(0, 1)
        self.layout_malt_weight.setStretch(2, 1)

        self.layout_malts_tab.addLayout(self.layout_malt_weight)

        self.btn_malt_add = QPushButton(self.tab_malts)
        self.btn_malt_add.setObjectName(u"btn_malt_add")
        self.btn_malt_add.setMinimumSize(QSize(0, 36))
        self.btn_malt_add.setFont(font3)
        self.btn_malt_add.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.layout_malts_tab.addWidget(self.btn_malt_add)

        self.layout_malts_tab.setStretch(0, 6)
        self.layout_malts_tab.setStretch(1, 1)
        self.layout_malts_tab.setStretch(2, 1)
        self.tab_widget_ingredients.addTab(self.tab_malts, "")
        self.tab_hops = QWidget()
        self.tab_hops.setObjectName(u"tab_hops")
        self.layout_hops_tab = QVBoxLayout(self.tab_hops)
        self.layout_hops_tab.setSpacing(6)
        self.layout_hops_tab.setObjectName(u"layout_hops_tab")
        self.tbl_hops = QTableWidget(self.tab_hops)
        self.tbl_hops.setObjectName(u"tbl_hops")
        self.tbl_hops.setMinimumSize(QSize(0, 120))
        self.tbl_hops.setFont(font9)

        self.layout_hops_tab.addWidget(self.tbl_hops)

        self.layout_hop_weight = QHBoxLayout()
        self.layout_hop_weight.setObjectName(u"layout_hop_weight")
        self.lbl_hop_weight = QLabel(self.tab_hops)
        self.lbl_hop_weight.setObjectName(u"lbl_hop_weight")
        self.lbl_hop_weight.setMinimumSize(QSize(65, 30))
        self.lbl_hop_weight.setMaximumSize(QSize(65, 30))
        self.lbl_hop_weight.setFont(font3)
        self.lbl_hop_weight.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.layout_hop_weight.addWidget(self.lbl_hop_weight)

        self.slider_hop_weight = QSlider(self.tab_hops)
        self.slider_hop_weight.setObjectName(u"slider_hop_weight")
        sizePolicy4.setHeightForWidth(self.slider_hop_weight.sizePolicy().hasHeightForWidth())
        self.slider_hop_weight.setSizePolicy(sizePolicy4)
        self.slider_hop_weight.setOrientation(Qt.Orientation.Horizontal)

        self.layout_hop_weight.addWidget(self.slider_hop_weight)

        self.edit_hop_weight = QLineEdit(self.tab_hops)
        self.edit_hop_weight.setObjectName(u"edit_hop_weight")
        self.edit_hop_weight.setMinimumSize(QSize(75, 30))
        self.edit_hop_weight.setMaximumSize(QSize(85, 30))
        self.edit_hop_weight.setFont(font3)
        self.edit_hop_weight.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.layout_hop_weight.addWidget(self.edit_hop_weight)

        self.layout_hop_weight.setStretch(0, 1)
        self.layout_hop_weight.setStretch(1, 10)
        self.layout_hop_weight.setStretch(2, 1)

        self.layout_hops_tab.addLayout(self.layout_hop_weight)

        self.layout_hop_time = QHBoxLayout()
        self.layout_hop_time.setObjectName(u"layout_hop_time")
        self.lbl_hop_time = QLabel(self.tab_hops)
        self.lbl_hop_time.setObjectName(u"lbl_hop_time")
        self.lbl_hop_time.setMinimumSize(QSize(65, 30))
        self.lbl_hop_time.setMaximumSize(QSize(65, 30))
        self.lbl_hop_time.setFont(font3)
        self.lbl_hop_time.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.layout_hop_time.addWidget(self.lbl_hop_time)

        self.slider_hop_time = QSlider(self.tab_hops)
        self.slider_hop_time.setObjectName(u"slider_hop_time")
        sizePolicy4.setHeightForWidth(self.slider_hop_time.sizePolicy().hasHeightForWidth())
        self.slider_hop_time.setSizePolicy(sizePolicy4)
        self.slider_hop_time.setOrientation(Qt.Orientation.Horizontal)

        self.layout_hop_time.addWidget(self.slider_hop_time)

        self.edit_hop_time = QLineEdit(self.tab_hops)
        self.edit_hop_time.setObjectName(u"edit_hop_time")
        self.edit_hop_time.setMinimumSize(QSize(75, 30))
        self.edit_hop_time.setMaximumSize(QSize(85, 30))
        self.edit_hop_time.setFont(font3)
        self.edit_hop_time.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.layout_hop_time.addWidget(self.edit_hop_time)

        self.layout_hop_time.setStretch(0, 1)
        self.layout_hop_time.setStretch(1, 10)
        self.layout_hop_time.setStretch(2, 1)

        self.layout_hops_tab.addLayout(self.layout_hop_time)

        self.btn_hop_add = QPushButton(self.tab_hops)
        self.btn_hop_add.setObjectName(u"btn_hop_add")
        self.btn_hop_add.setMinimumSize(QSize(0, 36))
        self.btn_hop_add.setFont(font3)
        self.btn_hop_add.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.layout_hops_tab.addWidget(self.btn_hop_add)

        self.layout_hops_tab.setStretch(0, 5)
        self.layout_hops_tab.setStretch(1, 1)
        self.layout_hops_tab.setStretch(2, 1)
        self.layout_hops_tab.setStretch(3, 1)
        self.tab_widget_ingredients.addTab(self.tab_hops, "")
        self.tab_yeasts = QWidget()
        self.tab_yeasts.setObjectName(u"tab_yeasts")
        self.layout_yeasts_tab = QVBoxLayout(self.tab_yeasts)
        self.layout_yeasts_tab.setSpacing(6)
        self.layout_yeasts_tab.setObjectName(u"layout_yeasts_tab")
        self.tbl_yeasts = QTableWidget(self.tab_yeasts)
        self.tbl_yeasts.setObjectName(u"tbl_yeasts")
        self.tbl_yeasts.setMinimumSize(QSize(0, 120))
        self.tbl_yeasts.setFont(font9)

        self.layout_yeasts_tab.addWidget(self.tbl_yeasts)

        self.btn_yeast_add = QPushButton(self.tab_yeasts)
        self.btn_yeast_add.setObjectName(u"btn_yeast_add")
        self.btn_yeast_add.setMinimumSize(QSize(0, 36))
        self.btn_yeast_add.setFont(font3)
        self.btn_yeast_add.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.layout_yeasts_tab.addWidget(self.btn_yeast_add)

        self.layout_yeasts_tab.setStretch(0, 7)
        self.layout_yeasts_tab.setStretch(1, 1)
        self.tab_widget_ingredients.addTab(self.tab_yeasts, "")

        self.layout_ingredients.addWidget(self.tab_widget_ingredients)


        self.layout_right_column.addWidget(self.frame_ingredients)

        self.layout_right_column.setStretch(0, 2)
        self.layout_right_column.setStretch(1, 6)

        self.layout_main.addLayout(self.layout_right_column)

        self.layout_main.setStretch(0, 6)
        self.layout_main.setStretch(1, 4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tab_widget_ingredients.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Beer Brewing Simulator", None))
        self.lbl_brewing_state_title.setText(QCoreApplication.translate("MainWindow", u"State", None))
        self.btn_reset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.btn_brewing_state_prev.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.btn_brewing_state_next.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.lbl_temperature_header.setText(QCoreApplication.translate("MainWindow", u"TEMP", None))
        self.lbl_temperature_value.setText(QCoreApplication.translate("MainWindow", u"100 \u02daC", None))
        self.btn_timeline_rewind.setText(QCoreApplication.translate("MainWindow", u"\u23ee", None))
        self.btn_timeline_play_pause.setText(QCoreApplication.translate("MainWindow", u"\u25b6", None))
        self.btn_timeline_fast_forward.setText(QCoreApplication.translate("MainWindow", u"\u23ed", None))
        self.lbl_timeline_time.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.lbl_summary_malts_title.setText(QCoreApplication.translate("MainWindow", u"Malts", None))
        self.lbl_summary_hops_title.setText(QCoreApplication.translate("MainWindow", u"Hops", None))
        self.lbl_summary_yeast_title.setText(QCoreApplication.translate("MainWindow", u"Yeast", None))
        self.lbl_summary_water_title.setText(QCoreApplication.translate("MainWindow", u"Batch Size", None))
        self.edit_summary_water.setPlaceholderText(QCoreApplication.translate("MainWindow", u"20 L", None))
        self.btn_summary_water_down.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.btn_summary_water_up.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.lbl_metric_og_title.setText(QCoreApplication.translate("MainWindow", u"OG", None))
        self.lbl_metric_og_value.setText(QCoreApplication.translate("MainWindow", u"1.035", None))
        self.lbl_metric_fg_title.setText(QCoreApplication.translate("MainWindow", u"FG", None))
        self.lbl_metric_fg_value.setText(QCoreApplication.translate("MainWindow", u"1.008", None))
        self.lbl_metric_color_title.setText(QCoreApplication.translate("MainWindow", u"Color", None))
        self.lbl_metric_srm_value.setText(QCoreApplication.translate("MainWindow", u"SRM: 9", None))
        self.lbl_metric_rgb_preview.setText(QCoreApplication.translate("MainWindow", u"RGB", None))
        self.lbl_metric_abv_title.setText(QCoreApplication.translate("MainWindow", u"ABV", None))
        self.lbl_metric_abv_value.setText(QCoreApplication.translate("MainWindow", u"5%", None))
        self.lbl_metric_ibu_title.setText(QCoreApplication.translate("MainWindow", u"IBU", None))
        self.lbl_metric_ibu_value.setText(QCoreApplication.translate("MainWindow", u"33", None))
        self.lbl_info_title.setText(QCoreApplication.translate("MainWindow", u"Title", None))
        self.lbl_info_description.setText(QCoreApplication.translate("MainWindow", u"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus pulvinar eu mauris vitae bibendum. In rutrum mauris nunc, id tempus justo fermentum nec. Sed id malesuada metus, a auctor quam. Suspendisse molestie tempor turpis et placerat. Nunc sit amet tristique metus. In a erat et ligula pharetra ultrices.", None))
        self.lbl_malt_weight.setText(QCoreApplication.translate("MainWindow", u"Weight", None))
        self.btn_malt_add.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.tab_widget_ingredients.setTabText(self.tab_widget_ingredients.indexOf(self.tab_malts), QCoreApplication.translate("MainWindow", u"Malts", None))
        self.lbl_hop_weight.setText(QCoreApplication.translate("MainWindow", u"Weight", None))
        self.lbl_hop_time.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.btn_hop_add.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.tab_widget_ingredients.setTabText(self.tab_widget_ingredients.indexOf(self.tab_hops), QCoreApplication.translate("MainWindow", u"Hops", None))
        self.btn_yeast_add.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.tab_widget_ingredients.setTabText(self.tab_widget_ingredients.indexOf(self.tab_yeasts), QCoreApplication.translate("MainWindow", u"Yeasts", None))
    # retranslateUi

