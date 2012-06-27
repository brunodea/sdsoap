#!/usr/bin/python
# -*- encoding: utf-8 -*-

import sys
import webbrowser
from PyQt4 import QtCore,QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s
    
class MainWindow2(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow2, self).__init__()
        self.search_button = None
        self.num_ebay_spinbox = None
        self.games_listview = None
        self.ebay_listview = None
        self.platform_combobox = None
        self.current_games = []
        self.current_game = None
        self.current_ebay = None
        self.search_line_edit = None
        self.to_ebay_button = None
        self.game_name_label = None
        self.center_image_label = None
        
    def init_ui(self):
        self.search_button = QtGui.QPushButton('Buscar')
        self.search_line_edit = QtGui.QLineEdit()
        search_label = QtGui.QLabel('Buscar')
        self.num_ebay_spinbox = QtGui.QSpinBox()
        self.num_ebay_spinbox.setMaximum(100)
        self.num_ebay_spinbox.setMinimum(1)
        
        search_layout = QtGui.QHBoxLayout()
        search_layout.addWidget(search_label, QtCore.Qt.AlignRight)
        search_layout.addWidget(self.search_line_edit, QtCore.Qt.AlignCenter)
        search_layout.addWidget(self.search_button, QtCore.Qt.AlignCenter)
        
        self.games_listview = QtGui.QListWidget()
        
        self.platform_combobox = QtGui.QComboBox()
        self.platform_combobox.setObjectName(_fromUtf8("platformCombobox"))

        games_layout = QtGui.QVBoxLayout()
        games_layout.addWidget(self.platform_combobox)
        games_layout.addWidget(self.games_listview, QtCore.Qt.AlignCenter)
        
              
        left_aux = QtGui.QWidget()
        left_aux.setLayout(games_layout)
        left_dock = QtGui.QDockWidget('Plataformas/Jogos')
        left_dock.setWidget(left_aux)

        self.addDockWidget(QtCore.Qt.TopDockWidgetArea,left_dock)
        
        no_img_pixmap = QtGui.QPixmap('imgs/no_image.png')
                
        self.center_image_label = QtGui.QLabel()
        self.center_image_label.setPixmap(no_img_pixmap)
        
        self.game_name_label = QtGui.QLabel('Nenhum Jogo Selecionado')
        
        self.ebay_listview = QtGui.QListWidget()
        self.to_ebay_button = QtGui.QPushButton('ver no eBay')
        
        self.to_ebay_button.clicked.connect(self.goToCurrentEbaySite)
        
        right_vbox_layout = QtGui.QVBoxLayout()
        right_vbox_layout.addWidget(QtGui.QLabel(_fromUtf8('Número máximo de retornos no ebay')))
        right_vbox_layout.addWidget(self.num_ebay_spinbox, QtCore.Qt.AlignRight)
        right_vbox_layout.addWidget(self.ebay_listview)
        right_vbox_layout.addWidget(self.to_ebay_button)
                
        right_aux = QtGui.QWidget()
        right_aux.setLayout(right_vbox_layout)
        right_dock = QtGui.QDockWidget('Jogo no eBay')
        right_dock.setWidget(right_aux)
        
        self.addDockWidget(QtCore.Qt.BottomDockWidgetArea,right_dock)
        
        center_hbox_layout = QtGui.QHBoxLayout()
        center_hbox_layout.addWidget(self.center_image_label, QtCore.Qt.AlignCenter)
        center_hbox_layout.addWidget(self.game_name_label, QtCore.Qt.AlignCenter)

        final_layout = QtGui.QVBoxLayout()
        final_layout.addLayout(search_layout)
        final_layout.addLayout(center_hbox_layout)
        
        center_aux = QtGui.QWidget()
        center_aux.setLayout(final_layout)
        self.setCentralWidget(center_aux)

        self.setWindowTitle(_fromUtf8('Sistemas Distubuídos T4'))
        statusbar = QtGui.QStatusBar()
        statusbar.showMessage('por Bruno Romero de Azevedo, Davi Felipe Russi, Matheus Depra Gudergues e Vitor da Silva.')
        self.setStatusBar(statusbar)
        self.show()
        
    def setSearchButtonCallback(self,callback_func):
        self.search_button.clicked.connect(callback_func)
    
    def setPlatformList(self, platform_list):
        self.platform_combobox.clear()
        self.platform_combobox.addItems(platform_list)
        
    def setGameList(self,game_list):
        self.games_listview.clear()
        self.games_listview.addItems(game_list)
        
    def setEbayList(self,ebay_list):
        self.ebay_listview.clear()
        self.ebay_listview.addItems(ebay_list)
        
    def setPlatformItemChangedCallback(self, callback_func):
        self.connect(self.platform_combobox,QtCore.SIGNAL("currentIndexChanged(const QString &)"),callback_func)
    
    def searchText(self):
        return self.search_line_edit.text()
        
    def setGameListItemChangedCallback(self, callback_func):
        self.games_listview.currentItemChanged.connect(callback_func)
        
    def setEbayListItemChangedCallback(self, callback_func):
        self.ebay_listview.currentItemChanged.connect(callback_func)
    
    def goToCurrentEbaySite(self):
        if not self.current_ebay == None:
            webbrowser.open(self.current_ebay.link_ebay,new=2)#abre em nova aba se possível
    
    def adjustCentralStuff(self):
        if self.current_game != None:
            text = '<h2>%s</h2> <br> <h3>%s</h3>'% (self.current_game.name,self.current_game.platform)
    
            if self.current_ebay != None:
                text = '%s<p> %s %s <p> <a href=\"%s\">eBay</a>' % \
                    (text, self.current_ebay.currency, self.current_ebay.price, \
                     self.current_ebay.link_ebay)
            self.game_name_label.setText('<qt>%s</qt>' % text)
        else:
            self.game_name_label.setText('Nenhum jogo selecionado')
            self.setCentraImage(None)
    
    def setCentralImage(self,image_path):
        pix = None
        if image_path != None:
            pix = QtGui.QPixmap(image_path)
        if pix != None:
            self.center_image_label.setPixmap(pix)
        else:
            pix = QtGui.QPixmap('imgs/no_image.png')
            self.center_image_label.setPixmap(pix)
    
    def numebay(self):
        return self.num_ebay_spinbox.value()
        
        
