# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ORWidget.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QLabel, QPushButton,
    QSizePolicy, QSlider, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_ORWidget(object):
    def setupUi(self, ORWidget):
        if not ORWidget.objectName():
            ORWidget.setObjectName(u"ORWidget")
        ORWidget.resize(786, 554)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(8)
        font.setBold(True)
        ORWidget.setFont(font)
        ORWidget.setMouseTracking(True)
        self.label = QLabel(ORWidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 10, 631, 521))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(1, 1))
        self.label.setCursor(QCursor(Qt.CrossCursor))
        self.label.setMouseTracking(True)
        self.label.setContextMenuPolicy(Qt.NoContextMenu)
        self.verticalLayoutWidget = QWidget(ORWidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(670, 10, 81, 151))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.readImageButton = QPushButton(self.verticalLayoutWidget)
        self.readImageButton.setObjectName(u"readImageButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.readImageButton.sizePolicy().hasHeightForWidth())
        self.readImageButton.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.readImageButton)

        self.moveButton = QPushButton(self.verticalLayoutWidget)
        self.buttonGroup = QButtonGroup(ORWidget)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.setExclusive(True)
        self.buttonGroup.addButton(self.moveButton)
        self.moveButton.setObjectName(u"moveButton")
        sizePolicy1.setHeightForWidth(self.moveButton.sizePolicy().hasHeightForWidth())
        self.moveButton.setSizePolicy(sizePolicy1)
        self.moveButton.setCheckable(True)
        self.moveButton.setChecked(True)
        self.moveButton.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.moveButton)

        self.drawRectButton = QPushButton(self.verticalLayoutWidget)
        self.buttonGroup.addButton(self.drawRectButton)
        self.drawRectButton.setObjectName(u"drawRectButton")
        sizePolicy1.setHeightForWidth(self.drawRectButton.sizePolicy().hasHeightForWidth())
        self.drawRectButton.setSizePolicy(sizePolicy1)
        self.drawRectButton.setCheckable(True)
        self.drawRectButton.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.drawRectButton)

        self.drawButton = QPushButton(self.verticalLayoutWidget)
        self.buttonGroup.addButton(self.drawButton)
        self.drawButton.setObjectName(u"drawButton")
        sizePolicy1.setHeightForWidth(self.drawButton.sizePolicy().hasHeightForWidth())
        self.drawButton.setSizePolicy(sizePolicy1)
        self.drawButton.setMouseTracking(False)
        self.drawButton.setCheckable(True)
        self.drawButton.setChecked(False)
        self.drawButton.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.drawButton)

        self.writeImageButton = QPushButton(self.verticalLayoutWidget)
        self.writeImageButton.setObjectName(u"writeImageButton")
        sizePolicy1.setHeightForWidth(self.writeImageButton.sizePolicy().hasHeightForWidth())
        self.writeImageButton.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.writeImageButton)

        self.mouseInfo = QTextBrowser(ORWidget)
        self.mouseInfo.setObjectName(u"mouseInfo")
        self.mouseInfo.setGeometry(QRect(670, 170, 81, 91))
        self.mouseInfo.setMouseTracking(False)
        self.undoButton = QPushButton(ORWidget)
        self.undoButton.setObjectName(u"undoButton")
        self.undoButton.setGeometry(QRect(670, 270, 75, 23))
        sizePolicy1.setHeightForWidth(self.undoButton.sizePolicy().hasHeightForWidth())
        self.undoButton.setSizePolicy(sizePolicy1)
        self.undoButton.setContextMenuPolicy(Qt.NoContextMenu)
        self.redoButton = QPushButton(ORWidget)
        self.redoButton.setObjectName(u"redoButton")
        self.redoButton.setGeometry(QRect(670, 300, 75, 23))
        sizePolicy1.setHeightForWidth(self.redoButton.sizePolicy().hasHeightForWidth())
        self.redoButton.setSizePolicy(sizePolicy1)
        self.setPenColorButton = QPushButton(ORWidget)
        self.setPenColorButton.setObjectName(u"setPenColorButton")
        self.setPenColorButton.setGeometry(QRect(670, 330, 75, 23))
        sizePolicy1.setHeightForWidth(self.setPenColorButton.sizePolicy().hasHeightForWidth())
        self.setPenColorButton.setSizePolicy(sizePolicy1)
        self.pen = QLabel(ORWidget)
        self.pen.setObjectName(u"pen")
        self.pen.setGeometry(QRect(700, 370, 10, 10))
        self.verticalSlider = QSlider(ORWidget)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setGeometry(QRect(670, 390, 71, 22))
        self.verticalSlider.setAutoFillBackground(False)
        self.verticalSlider.setMaximum(25)
        self.verticalSlider.setPageStep(3)
        self.verticalSlider.setValue(5)
        self.verticalSlider.setOrientation(Qt.Horizontal)

        self.retranslateUi(ORWidget)
        self.writeImageButton.clicked.connect(ORWidget.cv2Imwrite)
        self.readImageButton.clicked.connect(ORWidget.cv2Imread)
        self.undoButton.clicked.connect(ORWidget.undo)
        self.redoButton.clicked.connect(ORWidget.redo)
        self.setPenColorButton.clicked.connect(ORWidget.setPenColor)
        self.verticalSlider.valueChanged.connect(ORWidget.updatePen)

        QMetaObject.connectSlotsByName(ORWidget)
    # setupUi

    def retranslateUi(self, ORWidget):
        ORWidget.setWindowTitle(QCoreApplication.translate("ORWidget", u"ORWidget", None))
        self.label.setText("")
        self.readImageButton.setText(QCoreApplication.translate("ORWidget", u"\u8bfb\u5165\u56fe\u7247", None))
        self.moveButton.setText(QCoreApplication.translate("ORWidget", u"\u79fb\u52a8", None))
        self.drawRectButton.setText(QCoreApplication.translate("ORWidget", u"\u753b\u77e9\u5f62", None))
        self.drawButton.setText(QCoreApplication.translate("ORWidget", u"\u753b\u56fe", None))
        self.writeImageButton.setText(QCoreApplication.translate("ORWidget", u"\u5199\u56fe\u7247", None))
        self.mouseInfo.setHtml(QCoreApplication.translate("ORWidget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:8pt; font-weight:700; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.undoButton.setText(QCoreApplication.translate("ORWidget", u"\u64a4\u9500", None))
        self.redoButton.setText(QCoreApplication.translate("ORWidget", u"\u53cd\u5411\u64a4\u9500", None))
        self.setPenColorButton.setText(QCoreApplication.translate("ORWidget", u"\u8bbe\u7f6e\u989c\u8272", None))
        self.pen.setText("")
    # retranslateUi

