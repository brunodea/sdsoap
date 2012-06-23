

from PyQt4.QtGui import QMainWindow
from gui_mainwindow import Ui_MainWindow

class GUI(QMainWindow, Ui_MainWindow):
    def __init__(self):
		# Inicia a janela principal
        QMainWindow.__init__(self)
        # Inicia a UI criada no Qt Designer
        self.setupUi(self)
		