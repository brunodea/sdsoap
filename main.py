# -*- encoding: utf-8 -*-

import sys
from PyQt4.QtGui import QApplication
from PyQt4 import QtCore
from gui_v3 import GUIv3
import search
import getcover
import ebay
from threading import Thread


APP = QApplication(sys.argv)
THE_GUI = GUIv3()
IMAGE_PATH = ''

def gamesearch_thread():
    THE_GUI.current_games = search.getGamesFromSearch(THE_GUI.searchText())
    platforms = []
    for g in THE_GUI.current_games:
        if g.platform not in platforms:
                platforms.append(g.platform.decode('utf-8'))
    THE_GUI.setPlatformList(platforms)
    THE_GUI.statusBar().showMessage('Busca finalizada!')

def gamesearch(clicked):
    THE_GUI.statusBar().showMessage('Buscando...')
    th = Thread(target=gamesearch_thread())
    th.start()


def gamelistByPlatform(platform):
    gamesnames = []
    for g in THE_GUI.current_games:
        if g.platform == platform:
            gamesnames.append(g.name.decode('utf-8'))
    THE_GUI.setGameList(gamesnames)

def adjustEbayList(new_list_widget_item,last_list_widget_item):
    THE_GUI.current_game = None
    if new_list_widget_item == None:
        return
    
    for g in THE_GUI.current_games:
        if g.name == new_list_widget_item.text():
            print 'Buscando no eBay'
            g.ebay = ebay.getEBayItems('%s %s'%(g.name,g.platform),THE_GUI.numebay())
            print 'Busca no eBay finalizada.'
            THE_GUI.setEbayList([x.title for x in g.ebay])
            THE_GUI.current_game = g
            THE_GUI.statusBar().showMessage('Baixando imagem...')
            THE_GUI.setCentralImage(getcover.downloadcover(g.gameid,'imgs/cover'))    
            THE_GUI.statusBar().showMessage('Imagem baixada!')
            THE_GUI.adjustCentralStuff()
            break

def adjustCurrentEbay(new_list_widget_item,last_list_widget_item):
    THE_GUI.current_ebay = None
    if THE_GUI.current_game == None or new_list_widget_item == None:
        return
    
    for e in THE_GUI.current_game.ebay:
        if e.title == new_list_widget_item.text():
            THE_GUI.current_ebay = e
            THE_GUI.adjustCentralStuff()
            break

def updateCurrentEbay_thread():
    g = THE_GUI.current_game
    THE_GUI.current_game.ebay = ebay.getEBayItems('%s %s'%(g.name,g.platform),THE_GUI.numebay())
    THE_GUI.setEbayList([x.title for x in THE_GUI.current_game.ebay])
    print 'Busca no eBay finalizada.'

def updateCurrentEbay(spinbox_item):
    print 'Buscando no eBay'
    th = Thread(target=updateCurrentEbay_thread)
    th.start()

def main():
    #THE_GUI.init_ui()
    THE_GUI.setSearchButtonCallback(gamesearch)
    THE_GUI.setPlatformItemChangedCallback(gamelistByPlatform)
    THE_GUI.setGameListItemChangedCallback(adjustEbayList)
    THE_GUI.setEbayListItemChangedCallback(adjustCurrentEbay)
    THE_GUI.setNumResEbayChangedCallback(updateCurrentEbay)
    THE_GUI.show()
    
    sys.exit(APP.exec_())

if __name__ == '__main__':
    main()
