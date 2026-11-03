from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QPen, QColor, QBrush
from PySide6.QtCore import Qt, QRectF, QPointF


def draw_simulation(painter, width, height, volume = 0.0, max_volume= 40.0, liquid_color = None):

    painter.setRenderHint(QPainter.RenderHint.Antialiasing)

    # Outer vessel dimensions
    margin_x = int(width * 0.12)
    margin_top = int(height * 0.10)
    margin_bottom = int(height * 0.90)

    vessel_left = margin_x
    vessel_right = width - margin_x
    vessel_top = margin_top
    vessel_bottom = margin_bottom
    vessel_width = vessel_right - vessel_left
    vessel_height = vessel_bottom - vessel_top

    wall_thickness = 4

    # Inner volume rectangle
    fill_ratio = min(1.0, max(0.0, volume / max_volume)) if max_volume > 0 else 0.0
    inner_left = vessel_left + wall_thickness / 2.0 + 1
    inner_width = vessel_width - wall_thickness - 2
    max_liquid_h = vessel_height - wall_thickness / 2.0 - 2
    liquid_h = max_liquid_h * fill_ratio

    if liquid_h > 0:
        liquid_top = vessel_bottom - wall_thickness / 2.0 - liquid_h
        liquid_rect = QRectF(inner_left, liquid_top, inner_width, liquid_h)
        col = liquid_color if liquid_color else QColor(100, 180, 245, 170)
        painter.fillRect(liquid_rect, QBrush(col))

        surface_pen = QPen(col.darker(125), 2)
        painter.setPen(surface_pen)
        painter.drawLine(QPointF(inner_left, liquid_top), QPointF(inner_left + inner_width, liquid_top))

    # Outer vessel
    vessel_pen = QPen(QColor(70, 80, 90), wall_thickness, Qt.PenStyle.SolidLine, Qt.PenCapStyle.SquareCap, Qt.PenJoinStyle.MiterJoin)
    painter.setPen(vessel_pen)
    points = [
        QPointF(vessel_left, vessel_top),
        QPointF(vessel_left, vessel_bottom),
        QPointF(vessel_right, vessel_bottom),
        QPointF(vessel_right, vessel_top)
    ]
    painter.drawPolyline(points)

class SimulationVesselWidget(QWidget):
    def __init__(self, parent=None, max_volume = 40.0):
        super().__init__(parent)
        self.volume = 0.0
        self.max_volume = max_volume
        self.liquid_color = QColor(100, 180, 245, 170)

    def set_volume(self, volume):
        self.volume = float(volume)
        self.max_volume = max(self.max_volume, volume * 1.15)
        self.update()

    def set_color_from_srm(self, srm_hex=None):
        if not srm_hex:
            self.liquid_color = QColor(100, 180, 245, 170)
        else:
            qcol = QColor(srm_hex)
            qcol.setAlpha(190)
            self.liquid_color = qcol
        self.update()

    def set_state(self, volume, srm_hex = None):
        self.volume = float(volume)
        self.max_volume = max(self.max_volume, volume * 1.15)
        self.set_color_from_srm(srm_hex)

    def paintEvent(self, event):
        painter = QPainter(self)
        draw_simulation(painter, self.width(), self.height(), self.volume, self.max_volume, self.liquid_color)
        painter.end()
