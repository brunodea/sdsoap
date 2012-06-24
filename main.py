
import sys
from PyQt4.QtGui import QApplication
from PyQt4 import QtCore
from gui import GUI

def fun(gui):
    """ Acao de exemplo pro botao de busca :D
        gui: referencia a interface grafica
    """
    print 'Click test:'
    print gui.getConsoleValue()
    print gui.getGameValue()

def main():
    # Inicia o fluxo de controle do Qt
    app = QApplication(sys.argv)
    # Instancia uma GUI
    gui = GUI()
    # Mostra a janela
    list = ['Hello Kitty Online', 'Barbie Dress-Up', 'Teletubbies']
    gui.setConsoleList(list)
    gui.setGameList(list)
    gui.setButtonAction(fun, gui)
    gui.show()
    # Finaliza a execucao do Qt quando a janela e fechada
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()