# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 717)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 200, 781, 144))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_2.addWidget(self.label_4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setMinimumSize(QtCore.QSize(200, 0))
        self.label_5.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_2.addWidget(self.label_5)
        self.num_ebay_spinbox = QtGui.QSpinBox(self.layoutWidget)
        self.num_ebay_spinbox.setMinimumSize(QtCore.QSize(200, 0))
        self.num_ebay_spinbox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.num_ebay_spinbox.setProperty("value", 1)
        self.num_ebay_spinbox.setObjectName(_fromUtf8("num_ebay_spinbox"))
        self.horizontalLayout_2.addWidget(self.num_ebay_spinbox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.ebay_listview = QtGui.QListWidget(self.layoutWidget)
        self.ebay_listview.setObjectName(_fromUtf8("ebay_listview"))
        self.verticalLayout_2.addWidget(self.ebay_listview)
        self.center_image_label = QtGui.QLabel(self.centralwidget)
        self.center_image_label.setGeometry(QtCore.QRect(10, 350, 411, 311))
        self.center_image_label.setText(_fromUtf8(""))
        self.center_image_label.setPixmap(QtGui.QPixmap(_fromUtf8("imgs/no_image.png")))
        self.center_image_label.setObjectName(_fromUtf8("center_image_label"))
        self.game_name_label = QtGui.QLabel(self.centralwidget)
        self.game_name_label.setGeometry(QtCore.QRect(430, 350, 350, 281))
        self.game_name_label.setMinimumSize(QtCore.QSize(200, 0))
        self.game_name_label.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.game_name_label.setFont(font)
        self.game_name_label.setWordWrap(True)
        self.game_name_label.setObjectName(_fromUtf8("game_name_label"))
        self.layoutWidget1 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 10, 781, 29))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.search_layout = QtGui.QHBoxLayout(self.layoutWidget1)
        self.search_layout.setMargin(0)
        self.search_layout.setObjectName(_fromUtf8("search_layout"))
        self.label = QtGui.QLabel(self.layoutWidget1)
        self.label.setObjectName(_fromUtf8("label"))
        self.search_layout.addWidget(self.label)
        self.search_line_edit = QtGui.QLineEdit(self.layoutWidget1)
        self.search_line_edit.setObjectName(_fromUtf8("search_line_edit"))
        self.search_layout.addWidget(self.search_line_edit)
        self.search_button = QtGui.QPushButton(self.layoutWidget1)
        self.search_button.setObjectName(_fromUtf8("search_button"))
        self.search_layout.addWidget(self.search_button)
        self.layoutWidget2 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 50, 781, 144))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(self.layoutWidget2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_3 = QtGui.QLabel(self.layoutWidget2)
        self.label_3.setMinimumSize(QtCore.QSize(80, 0))
        self.label_3.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.platform_combobox = QtGui.QComboBox(self.layoutWidget2)
        self.platform_combobox.setMinimumSize(QtCore.QSize(250, 0))
        self.platform_combobox.setMaximumSize(QtCore.QSize(250, 16777215))
        self.platform_combobox.setFrame(True)
        self.platform_combobox.setObjectName(_fromUtf8("platform_combobox"))
        self.horizontalLayout.addWidget(self.platform_combobox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.games_listview = QtGui.QListWidget(self.layoutWidget2)
        self.games_listview.setObjectName(_fromUtf8("games_listview"))
        self.verticalLayout.addWidget(self.games_listview)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "eBay", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Numero maximo de retornos", None, QtGui.QApplication.UnicodeUTF8))
        self.game_name_label.setText(QtGui.QApplication.translate("MainWindow", "Nenhum jogo selecionado.", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Jogo", None, QtGui.QApplication.UnicodeUTF8))
        self.search_button.setText(QtGui.QApplication.translate("MainWindow", "Buscar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Resultados", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Plataforma", None, QtGui.QApplication.UnicodeUTF8))

