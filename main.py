
import sys
from PyQt4.QtGui import QApplication
from gui import GUI

def main():
    # Inicia o fluxo de controle do Qt
    app = QApplication(sys.argv)
    # Instancia uma GUI
    gui = GUI()
    # Mostra a janela
    list = ['Hello Kitty Online', 'Barbie Dress-Up', 'Teletubbies']
    gui.setGameList(list)
    gui.show()
    # Finaliza a execucao do Qt quando a janela e fechada
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()