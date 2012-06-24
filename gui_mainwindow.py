# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Sat Jun 23 17:38:16 2012
#      by: PyQt4 UI code generator 4.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(662, 437)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.leNameSearch = QtGui.QLineEdit(self.centralwidget)
        self.leNameSearch.setGeometry(QtCore.QRect(90, 10, 211, 20))
        self.leNameSearch.setObjectName(_fromUtf8("leNameSearch"))
        self.cbConsoleList = QtGui.QComboBox(self.centralwidget)
        self.cbConsoleList.setGeometry(QtCore.QRect(370, 10, 161, 22))
        self.cbConsoleList.setObjectName(_fromUtf8("cbConsoleList"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(320, 10, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.btSearch = QtGui.QPushButton(self.centralwidget)
        self.btSearch.setGeometry(QtCore.QRect(560, 10, 75, 23))
        self.btSearch.setObjectName(_fromUtf8("btSearch"))
        self.gameList = QtGui.QListView(self.centralwidget)
        self.gameList.setGeometry(QtCore.QRect(10, 70, 151, 321))
        self.gameList.setObjectName(_fromUtf8("gameList"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 50, 46, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(190, 70, 121, 161))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.gameName = QtGui.QLabel(self.centralwidget)
        self.gameName.setGeometry(QtCore.QRect(320, 70, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.gameName.setFont(font)
        self.gameName.setObjectName(_fromUtf8("gameName"))
        self.gamePrice = QtGui.QLabel(self.centralwidget)
        self.gamePrice.setGeometry(QtCore.QRect(500, 190, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.gamePrice.setFont(font)
        self.gamePrice.setObjectName(_fromUtf8("gamePrice"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(190, 240, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.graphicsView_2 = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(200, 280, 131, 101))
        self.graphicsView_2.setObjectName(_fromUtf8("graphicsView_2"))
        self.graphicsView_3 = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView_3.setGeometry(QtCore.QRect(350, 280, 131, 101))
        self.graphicsView_3.setObjectName(_fromUtf8("graphicsView_3"))
        self.graphicsView_4 = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView_4.setGeometry(QtCore.QRect(500, 280, 131, 101))
        self.graphicsView_4.setObjectName(_fromUtf8("graphicsView_4"))
        self.gameInfo = QtGui.QLabel(self.centralwidget)
        self.gameInfo.setGeometry(QtCore.QRect(320, 120, 46, 13))
        self.gameInfo.setObjectName(_fromUtf8("gameInfo"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 662, 18))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Trabalho 4 - Sistemas Distribuídos", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Nome do jogo", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Console", None, QtGui.QApplication.UnicodeUTF8))
        self.btSearch.setText(QtGui.QApplication.translate("MainWindow", "Buscar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Jogos", None, QtGui.QApplication.UnicodeUTF8))
        self.gameName.setText(QtGui.QApplication.translate("MainWindow", "Nome do Jogo", None, QtGui.QApplication.UnicodeUTF8))
        self.gamePrice.setText(QtGui.QApplication.translate("MainWindow", "US$99,99", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Screenshots", None, QtGui.QApplication.UnicodeUTF8))
        self.gameInfo.setText(QtGui.QApplication.translate("MainWindow", "Info", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbout.setTitle(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))

