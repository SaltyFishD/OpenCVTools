import sys
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtUiTools import QUiLoader
import ui
import cv2
import numpy as np


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.scale = 1.
        self._cur_pos = None
        self._start_pos = QtCore.QPoint()
        self._label_pos = QtCore.QPoint()
        self._Qim_src = None
        self._tmp = None
        self._cur_undo_list = -1
        self._undo_list = []
        self.painter = QtGui.QPainter(self)
        self.ui = ui.Ui_ORWidget()
        self.ui.setupUi(self)

    def cv2Imread(self):
        im = cv2.imread("IMG.jpg")
        im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
        self._Qim_src = QtGui.QImage(im.data, im.shape[1], im.shape[0], QtGui.QImage.Format_RGB888)
        self._undo_list.append(self._Qim_src)
        self._cur_undo_list = 0

        self.ui.label.setScaledContents(True)
        self.ui.label.setGeometry(100, 30, self._Qim_src.width(), self._Qim_src.height())
        self.ui.label.setPixmap(QtGui.QPixmap.fromImage(self._Qim_src))

    def cv2Imwrite(self):
        ap = self._undo_list[self._cur_undo_list].bits()
        im = np.array(ap)
        im.resize((self._undo_list[self._cur_undo_list].height(), self._undo_list[self._cur_undo_list].width(), 3))
        im = cv2.cvtColor(im, cv2.COLOR_RGB2BGR)
        cv2.imshow("image", im)
        cv2.waitKey(0)

    def global_pos_2_img_pos(self, global_pos):
        return (global_pos - self.ui.label.pos()) * self._Qim_src.width() / self.ui.label.width()

    def get_mouse_info(self, cur_pos):
        pos = self.global_pos_2_img_pos(cur_pos)
        x, y = np.clip(pos.x(), 0, self._undo_list[self._cur_undo_list].width() - 1), \
               np.clip(pos.y(), 0, self._undo_list[self._cur_undo_list].height() - 1)
        color = self._undo_list[self._cur_undo_list].pixelColor(x, y)
        self.ui.mouseInfo.setText("( {}, {} )\nr: {}\ng: {}\nb: {}\n"
                                  .format(x, y, color.red(), color.green(), color.blue()))

    def draw(self, cur_pos):
        self.painter.begin(self._undo_list[self._cur_undo_list])
        self.painter.setPen(QtGui.QPen(QtCore.Qt.red, self.ui.verticalSlider.value()))
        self.painter.setBrush(QtGui.QColor(QtCore.Qt.red))
        pos = self.global_pos_2_img_pos(cur_pos)
        line = QtCore.QLine(self.global_pos_2_img_pos(self._start_pos), pos)
        self.painter.drawLine(line)
        rect = QtCore.QRect(pos.x() - self.ui.verticalSlider.value() // 4,
                            pos.y() - self.ui.verticalSlider.value() // 4,
                            self.ui.verticalSlider.value() // 2,
                            self.ui.verticalSlider.value() // 2)
        self.painter.drawEllipse(rect)
        self.painter.end()
        self._start_pos = cur_pos

    def drawRect(self, cur_pos):
        self._tmp = self._undo_list[self._cur_undo_list].copy()
        self.painter.begin(self._tmp)
        self.painter.setPen(QtGui.QPen(QtCore.Qt.red, self.ui.verticalSlider.value()))
        rect = QtCore.QRect(self.global_pos_2_img_pos(self._start_pos),
                            self.global_pos_2_img_pos(cur_pos))
        self.painter.drawRect(rect)
        self.painter.end()

    def mousePressEvent(self, event):
        self._start_pos = event.position().toPoint()
        if self.ui.moveButton.isChecked():
            self._label_pos = self.ui.label.pos()

        # 画图需要新建图层
        if (self.ui.drawButton.isChecked() or self.ui.drawRectButton.isChecked()) and self._undo_list is not None:
            del (self._undo_list[self._cur_undo_list + 1:])
            Qim = self._undo_list[self._cur_undo_list].copy()
            self._undo_list.append(Qim)
            self._cur_undo_list = self._cur_undo_list + 1

    def mouseMoveEvent(self, event):
        if self._cur_undo_list == -1:
            return
        self._cur_pos = event.position().toPoint()
        self.get_mouse_info(event.position().toPoint())
        if self.ui.moveButton.isChecked() and event.buttons() == QtCore.Qt.LeftButton:
            self.ui.label.move(self._label_pos - self._start_pos + event.position().toPoint())

        # 任意画
        if self.ui.drawButton.isChecked() and event.buttons() == QtCore.Qt.LeftButton:
            self.draw(event.position().toPoint())
            self.ui.label.setPixmap(QtGui.QPixmap.fromImage(self._undo_list[self._cur_undo_list]))

        # 画矩形
        if self.ui.drawRectButton.isChecked() and event.buttons() == QtCore.Qt.LeftButton:
            self.drawRect(event.position().toPoint())
            self.ui.label.setPixmap(QtGui.QPixmap.fromImage(self._tmp))

    def mouseReleaseEvent(self, event):
        if self.ui.drawRectButton.isChecked():
            self._undo_list[self._cur_undo_list] = self._tmp.copy()

    def wheelEvent(self, event):
        if self._cur_undo_list == -1:
            return
        if (self.scale < 0.125 and event.angleDelta().y() < 0) or \
                (self.scale > 8 and event.angleDelta().y() > 0):
            return
        zoom = 1 + event.angleDelta().y() / 2000
        self.scale = self.scale * zoom
        offset = (self._cur_pos - self.ui.label.pos()) * zoom
        self.ui.label.setGeometry(self._cur_pos.x() - offset.x(),
                                  self._cur_pos.y() - offset.y(),
                                  self._Qim_src.width() * self.scale,
                                  self._Qim_src.height() * self.scale)

    def undo(self):
        if self._cur_undo_list > 0:
            self._cur_undo_list = self._cur_undo_list - 1
            self.ui.label.setPixmap(QtGui.QPixmap.fromImage(self._undo_list[self._cur_undo_list]))

    def redo(self):
        if self._cur_undo_list < len(self._undo_list) - 1:
            self._cur_undo_list = self._cur_undo_list + 1
            self.ui.label.setPixmap(QtGui.QPixmap.fromImage(self._undo_list[self._cur_undo_list]))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
