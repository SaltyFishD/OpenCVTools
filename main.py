import sys
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtUiTools import QUiLoader
import ui
import cv2
import numpy as np


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self._start_pos = QtCore.QPoint()
        self._label_pos = QtCore.QPoint()
        self._Qim_src = None
        self._tmp = None
        self._cur_undo_list = -1
        self._undo_list = []
        self.ui = ui.Ui_ORWidget()
        self.ui.setupUi(self)

    def cv2Imread(self):
        im = cv2.imread("IMG.jpg")
        im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
        self._tmp = QtGui.QImage(im.shape[1], im.shape[0], QtGui.QImage.Format_RGB888)
        self._Qim_src = QtGui.QImage(im.data, im.shape[1], im.shape[0], QtGui.QImage.Format_RGB888)
        self._undo_list.append(self._Qim_src)
        self._cur_undo_list = 0
        self.ui.label.setGeometry(100, 30, self._Qim_src.width(), self._Qim_src.height())
        self.ui.label.setPixmap(QtGui.QPixmap.fromImage(self._Qim_src))

    def cv2Imwrite(self):
        ap = self._undo_list[self._cur_undo_list].bits()
        im = np.array(ap)
        im.resize((self._undo_list[self._cur_undo_list].height(), self._undo_list[self._cur_undo_list].width(), 3))
        im = cv2.cvtColor(im, cv2.COLOR_RGB2BGR)
        cv2.imshow("image", im)
        cv2.waitKey(0)

    def get_mouse_info(self, cur_pos):
        pos = cur_pos - self.ui.label.pos()
        x, y = np.clip(pos.x(), 0, self._undo_list[self._cur_undo_list].width() - 1), \
               np.clip(pos.y(), 0, self._undo_list[self._cur_undo_list].height() - 1)
        color = self._undo_list[self._cur_undo_list].pixelColor(x, y)
        self.ui.mouseInfo.setText("x: {}\ny: {}\nr: {}\ng: {}\nb: {}\n"
                                  .format(x, y, color.red(), color.green(), color.blue()))

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
        self.get_mouse_info(event.position().toPoint())
        if self.ui.moveButton.isChecked() and event.buttons() == QtCore.Qt.LeftButton:
            self.ui.label.move(self._label_pos - self._start_pos + event.position().toPoint())

        # 任意画
        if self.ui.drawButton.isChecked() and event.buttons() == QtCore.Qt.LeftButton:
            painter = QtGui.QPainter(self)
            painter.begin(self._undo_list[self._cur_undo_list])
            painter.setPen(QtGui.QPen(QtCore.Qt.red, self.ui.verticalSlider.value()))
            painter.setBrush(QtGui.QColor(QtCore.Qt.red))
            offset = self.ui.label.pos()
            line = QtCore.QLine(self._start_pos - offset, event.position().toPoint() - offset)
            painter.drawLine(line)

            center = event.position().toPoint() - offset
            rect = QtCore.QRect(center.x() - self.ui.verticalSlider.value() // 4,
                                center.y() - self.ui.verticalSlider.value() // 4,
                                self.ui.verticalSlider.value() // 2,
                                self.ui.verticalSlider.value() // 2)
            painter.drawEllipse(rect)
            painter.end()
            self._start_pos = event.position().toPoint()
            self.ui.label.setPixmap(QtGui.QPixmap.fromImage(self._undo_list[self._cur_undo_list]))

        # 画矩形
        if self.ui.drawRectButton.isChecked() and event.buttons() == QtCore.Qt.LeftButton:
            painter = QtGui.QPainter(self)
            self._tmp.bits()[:] = self._undo_list[self._cur_undo_list].bits()[:]
            painter.begin(self._tmp)
            painter.setPen(QtGui.QPen(QtCore.Qt.red, self.ui.verticalSlider.value()))
            offset = self.ui.label.pos()
            rect = QtCore.QRect(self._start_pos - offset,
                                event.position().toPoint() - offset)
            painter.drawRect(rect)
            painter.end()
            self.ui.label.setPixmap(QtGui.QPixmap.fromImage(self._tmp))

    def mouseReleaseEvent(self, e):
        if self.ui.drawRectButton.isChecked():
            self._undo_list[self._cur_undo_list] = self._tmp.copy()

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

