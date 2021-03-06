#!/usr/bin/python
# -*- encoding: utf-8 -*-

import sys
import webbrowser
from PyQt4 import QtCore, QtGui
from gui_mainwindow import Ui_MainWindow
    
class GUIv3(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        # Inicia a janela principal
        QtGui.QMainWindow.__init__(self)
        # Inicia a UI criada no Qt Designer
        self.setupUi(self)
        self.statusBar().showMessage('Aguardando busca...')
        self.current_games = []
        self.current_game = None
        self.current_ebay = None
        
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
    
    def setNumResEbayChangedCallback(self, callback_func):
        self.connect(self.num_ebay_spinbox, QtCore.SIGNAL("valueChanged(int)"),callback_func)
    
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
            self.game_name_label.setOpenExternalLinks(True)
        else:
            self.game_name_label.setText('Nenhum jogo selecionado')
            self.setCentralImage(None)
    
    def setCentralImage(self,image_path):
        pix = None
        if image_path != None and image_path != '':
                pix = QtGui.QPixmap(image_path)
                
                if pix != None:
                    if pix.isNull():
                        pix = None
                    else:
                        pix = pix.scaled(410,308,aspectRatioMode=QtCore.Qt.KeepAspectRatio)
        if pix == None:
            pix = QtGui.QPixmap('imgs/no_image.png')
        if pix != None:          
            self.center_image_label.setPixmap(pix)
    
    def numebay(self):
        return self.num_ebay_spinbox.value()
        
        
