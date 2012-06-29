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


class Worker(QtCore.QThread):
    finished = QtCore.pyqtSignal()
    work = None
    args = None
    def __init__(self, parent=None):
        super(Worker,self).__init__(parent)

    def run(self):
        self.work(*self.args)
        self.finished.emit()

IMAGE_THREAD = Worker(THE_GUI)
EBAY_LIST_THREAD = Worker(THE_GUI)
GAME_SEARCH_THREAD = Worker(THE_GUI)
UPDATE_CURRENT_EBAY = Worker(THE_GUI)

def gamesearch_finished():
    global THE_GUI
    GAME_SEARCH_THREAD.quit()
    THE_GUI.statusBar().showMessage('Busca no GameCompare finalizada!')

def gamesearch_thread():
    global THE_GUI
    THE_GUI.current_games = search.getGamesFromSearch(THE_GUI.searchText())
    platforms = []
    for g in THE_GUI.current_games:
        if g.platform not in platforms:
                platforms.append(g.platform.decode('utf-8'))
    THE_GUI.setPlatformList(platforms)

def gamesearch(clicked):
    global THE_GUI
    global GAME_SEARCH_THREAD
    GAME_SEARCH_THREAD.quit()
    THE_GUI.current_game = None
    THE_GUI.adjustCentralStuff()
    THE_GUI.setCentralImage(None)
    THE_GUI.statusBar().showMessage('Buscando no GameCompare...')
    GAME_SEARCH_THREAD.finished.connect(gamesearch_finished)
    GAME_SEARCH_THREAD.work = gamesearch_thread
    GAME_SEARCH_THREAD.args = ()
    GAME_SEARCH_THREAD.start()


def gamelistByPlatform(platform):
    global THE_GUI
    gamesnames = []
    for g in THE_GUI.current_games:
        if g.platform == platform:
            gamesnames.append(g.name.decode('utf-8'))
    THE_GUI.setGameList(gamesnames)

def downloadImage_finished():
    global THE_GUI
    global IMAGE_PATH
    IMAGE_THREAD.quit()
    THE_GUI.statusBar().showMessage('Imagem baixada!')
    THE_GUI.adjustCentralStuff()
    THE_GUI.setCentralImage(IMAGE_PATH)

def downloadImage(gameid):
    global IMAGE_PATH
    IMAGE_PATH = getcover.downloadcover(gameid,'imgs/cover')
    
def adjustEbayList_finished():
    global THE_GUI
    global IMAGE_THREAD
    EBAY_LIST_THREAD.quit()
    IMAGE_THREAD.quit()
    THE_GUI.statusBar().showMessage('Buscando no eBay finalizada!')
    if THE_GUI.current_game == None:
        return
    IMAGE_THREAD.finished.connect(downloadImage_finished)
    IMAGE_THREAD.args = (THE_GUI.current_game.gameid,)
    IMAGE_THREAD.work = downloadImage
    THE_GUI.statusBar().showMessage('Baixando imagem...')
    IMAGE_THREAD.start()

def adjustEbayList(new_list_widget_item,last_list_widget_item):
    global THE_GUI
    THE_GUI.current_game = None
    if new_list_widget_item == None:
        return
    
    for g in THE_GUI.current_games:
        if g.name == new_list_widget_item.text():
            if len(g.ebay) != THE_GUI.numebay():
                print 'Buscando no eBay'
                g.ebay = ebay.getEBayItems('%s %s'%(g.name,g.platform),THE_GUI.numebay())
                print 'Busca no eBay finalizada.'
            THE_GUI.current_game = g
            THE_GUI.setEbayList([x.title for x in g.ebay])
            break

def adjustEbayList_aux(new_list_widget_item,last_list_widget_item):
    global THE_GUI
    global EBAY_LIST_THREAD
    THE_GUI.current_game = None
    THE_GUI.adjustCentralStuff()
    THE_GUI.setCentralImage(None)
    EBAY_LIST_THREAD.quit()
    EBAY_LIST_THREAD.finished.connect(adjustEbayList_finished)
    EBAY_LIST_THREAD.args = (new_list_widget_item,last_list_widget_item)
    EBAY_LIST_THREAD.work = adjustEbayList
    THE_GUI.statusBar().showMessage('Buscando no eBay...')
    EBAY_LIST_THREAD.start()

def adjustCurrentEbay(new_list_widget_item,last_list_widget_item):
    global THE_GUI
    THE_GUI.current_ebay = None
    if THE_GUI.current_game == None or new_list_widget_item == None:
        return
    
    for e in THE_GUI.current_game.ebay:
        if e.title == new_list_widget_item.text():
            THE_GUI.current_ebay = e
            THE_GUI.adjustCentralStuff()
            break

def updateCurrentEbay_finished():
    global THE_GUI
    global UPDATE_CURRENT_EBAY
    THE_GUI.statusBar().showMessage('Busca no eBay finalizada!')

def updateCurrentEbay_thread():
    global THE_GUI
    g = THE_GUI.current_game
    print 'Buscando no eBay'
    THE_GUI.current_game.ebay = ebay.getEBayItems('%s %s'%(g.name,g.platform),THE_GUI.numebay())
    THE_GUI.setEbayList([x.title for x in THE_GUI.current_game.ebay])
    print 'Busca no eBay finalizada.'

def updateCurrentEbay(spinbox_item):
    global THE_GUI
    global UPDATE_CURRENT_EBAY
    UPDATE_CURRENT_EBAY.quit()
    UPDATE_CURRENT_EBAY.work = updateCurrentEbay_thread
    UPDATE_CURRENT_EBAY.args = ()
    UPDATE_CURRENT_EBAY.finished.connect(updateCurrentEbay_finished)
    THE_GUI.statusBar().showMessage('Buscando no eBay...')
    UPDATE_CURRENT_EBAY.start()

def main():
    global THE_GUI
    THE_GUI.setSearchButtonCallback(gamesearch)
    THE_GUI.setPlatformItemChangedCallback(gamelistByPlatform)
    THE_GUI.setGameListItemChangedCallback(adjustEbayList_aux)
    THE_GUI.setEbayListItemChangedCallback(adjustCurrentEbay)
    THE_GUI.setNumResEbayChangedCallback(updateCurrentEbay)
    THE_GUI.show()
    
    sys.exit(APP.exec_())

if __name__ == '__main__':
    main()
