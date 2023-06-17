# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDateTimeEdit, QGraphicsView,
    QMainWindow, QProgressBar, QSizePolicy, QTextEdit,
    QWidget)

from analoggaugewidget import AnalogGaugeWidget
import Resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1114, 509)
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/car.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet(u"\n"
"QWidget#centralwidget{\n"
"border-image: url(:/backgrounds/2.jpg) 0 0 0 0 stretch stretch;\n"
"background-image: no-repeat;\n"
"background-image: contain;\n"
"}\n"
"")
        MainWindow.setAnimated(True)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setAutoFillBackground(False)
        self.speed = AnalogGaugeWidget(self.centralwidget)
        self.speed.setObjectName(u"speed")
        self.speed.setGeometry(QRect(410, 190, 300, 300))
        self.speed.setStyleSheet(u"")
        self.battery = AnalogGaugeWidget(self.centralwidget)
        self.battery.setObjectName(u"battery")
        self.battery.setGeometry(QRect(930, 310, 150, 150))
        self.dateTimeEdit = QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setEnabled(True)
        self.dateTimeEdit.setGeometry(QRect(840, 40, 220, 40))
        self.dateTimeEdit.setMaximumSize(QSize(220, 40))
        font1 = QFont()
        font1.setFamilies([u"Perpetua"])
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setItalic(True)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        font1.setKerning(False)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.dateTimeEdit.setFont(font1)
        self.dateTimeEdit.setAutoFillBackground(False)
        self.dateTimeEdit.setStyleSheet(u"color: rgb(0, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.dateTimeEdit.setInputMethodHints(Qt.ImhNone)
        self.dateTimeEdit.setWrapping(True)
        self.dateTimeEdit.setFrame(False)
        self.dateTimeEdit.setReadOnly(True)
        self.dateTimeEdit.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.dateTimeEdit.setKeyboardTracking(False)
        self.dateTimeEdit.setProperty("showGroupSeparator", False)
        self.dateTimeEdit.setCurrentSection(QDateTimeEdit.DaySection)
        self.dateTimeEdit.setCalendarPopup(False)
        self.dateTimeEdit.setCurrentSectionIndex(0)
        self.Title = QTextEdit(self.centralwidget)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(340, 10, 451, 81))
        font2 = QFont()
        font2.setFamilies([u"Monotype Corsiva"])
        font2.setPointSize(20)
        font2.setBold(True)
        self.Title.setFont(font2)
        self.Title.setStyleSheet(u"\n"
"background-image: url(:/backgrounds/1.jpg);\n"
"border-image: url(:/background/1.jpg) 0 0 0 0 stretch stretch;")
        self.Title.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Title.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(410, 130, 301, 50))
        self.textEdit.setAutoFillBackground(False)
        self.textEdit.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_2 = QTextEdit(self.centralwidget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(930, 260, 151, 40))
        self.textEdit_2.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.temp = AnalogGaugeWidget(self.centralwidget)
        self.temp.setObjectName(u"temp")
        self.temp.setGeometry(QRect(30, 310, 150, 150))
        self.textEdit_3 = QTextEdit(self.centralwidget)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(30, 260, 151, 40))
        font3 = QFont()
        font3.setFamilies([u"Marlett"])
        font3.setPointSize(10)
        self.textEdit_3.setFont(font3)
        self.textEdit_3.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.textEdit_4 = QTextEdit(self.centralwidget)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(30, 110, 321, 41))
        self.textEdit_4.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(930, 470, 150, 25))
        font4 = QFont()
        font4.setPointSize(8)
        font4.setBold(False)
        font4.setItalic(True)
        self.progressBar.setFont(font4)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"color: rgb(0, 70, 103);")
        self.progressBar.setValue(24)
        self.progressBar.setOrientation(Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)
        self.textEdit_5 = QTextEdit(self.centralwidget)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setGeometry(QRect(30, 10, 301, 87))
        self.textEdit_5.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.textEdit_5.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_5.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_6 = QTextEdit(self.centralwidget)
        self.textEdit_6.setObjectName(u"textEdit_6")
        self.textEdit_6.setGeometry(QRect(30, 150, 321, 87))
        self.textEdit_6.setStyleSheet(u"background-color: rgb(130, 130, 130);")
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(1000, 120, 71, 61))
        self.graphicsView.setStyleSheet(u"background-color: rgb(157, 157, 157);\n"
"\n"
"border-image: url(:/light/light-bulb-on.png);\n"
"border-image: url(:/light/lightbulb.png);")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.Title.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Monotype Corsiva'; font-size:20pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt; color:#ffffff; vertical-align:sub;\">Infrotainment system Dashboard</span></p></body></html>", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#ffffff;\">SPEED</span></p></body></html>", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffffff;\">BATTERY</span></p></body></html>", None))
        self.textEdit_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Marlett'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; color:#ffffff;\">TEMPRETURE</span></p></body></html>", None))
        self.textEdit_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#fefefe;\">Gairo Scope Reading</span></p></body></html>", None))
        self.textEdit_5.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#55aaff;\">ITI Graduation Project</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#55aaff;\">infotainmentsystem</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#55aaff;\">intake 2023</span></p></body></html>", None))
    # retranslateUi

