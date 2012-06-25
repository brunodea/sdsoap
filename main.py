# -*- encoding: utf-8 -*-

import sys
from PyQt4.QtGui import QApplication
from PyQt4 import QtCore
from gui import GUI
import search

def gamesearch(gui):
    """ Acao para o botao de busca
        gui: referencia a interface grafica
    """
    gui.current_games = search.getGamesFromSearch(gui.getGameValue())
    platforms = []
    for g in gui.current_games:
        if g.platform not in platforms:
                platforms.append(g.platform.decode('utf-8'))
    gui.setConsoleList(platforms)

def gamelistByPlatform(platform, gui):
    gamesnames = []
    for g in gui.current_games:
        if g.platform == platform:
            gamesnames.append(g.name.decode('utf-8'))
    gui.setGameList(gamesnames)

def main():
    app = QApplication(sys.argv)
    gui = GUI()
    gui.setButtonAction(gamesearch, gui)
    gui.setConsoleChangeAction(gamelistByPlatform)
    gui.show()
    # Finaliza a execucao do Qt quando a janela e fechada
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
