# -*- encoding: utf-8 -*-

import sys
from PyQt4.QtGui import QApplication
from PyQt4 import QtCore
from gui_mainwindow2 import MainWindow2
import search


APP = QApplication(sys.argv)
THE_GUI = MainWindow2()

def gamesearch(clicked):
    """ Acao para o botao de busca
        gui: referencia a interface grafica
    """
    THE_GUI.statusBar().showMessage('Buscando...')
    THE_GUI.current_games = search.getGamesFromSearch(THE_GUI.searchText(),3)
    platforms = []
    for g in THE_GUI.current_games:
        if g.platform not in platforms:
                platforms.append(g.platform.decode('utf-8'))
    THE_GUI.setPlatformList(platforms)
    THE_GUI.statusBar().showMessage('Busca finalizada!')

def gamelistByPlatform(platform):
    gamesnames = []
    for g in THE_GUI.current_games:
        if g.platform == platform:
            gamesnames.append(g.name.decode('utf-8'))
    THE_GUI.setGameList(gamesnames)

def adjustEbayList(new_list_widget_item,last_list_widget_item):
    THE_GUI.current_game = None
    for g in THE_GUI.current_games:
        if g.name == new_list_widget_item.text():        
            THE_GUI.setEbayList([x.title for x in g.ebay])
            THE_GUI.current_game = g
            THE_GUI.adjustCentralStuff()
            break

def adjustCurrentEbay(new_list_widget_item,last_list_widget_item):
    THE_GUI.current_ebay = None
    if THE_GUI.current_game == None:
        return
    
    for e in THE_GUI.current_game.ebay:
        if e.title == new_list_widget_item.text():
            THE_GUI.current_ebay = e
            THE_GUI.adjustCentralStuff()
            break

def main():
    THE_GUI.init_ui()
    THE_GUI.setSearchButtonCallback(gamesearch)
    THE_GUI.setPlatformItemChangedCallback(gamelistByPlatform)
    THE_GUI.setGameListItemChangedCallback(adjustEbayList)
    THE_GUI.setEbayListItemChangedCallback(adjustCurrentEbay)
    
    sys.exit(APP.exec_())

if __name__ == '__main__':
    main()
