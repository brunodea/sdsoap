
import sys
from PyQt4.QtCore import * #QAbstractListModel, QModelIndex
from PyQt4.QtGui import QMainWindow
from gui_mainwindow import Ui_MainWindow

class GUI(QMainWindow, Ui_MainWindow):

    def __init__(self):
		# Inicia a janela principal
        QMainWindow.__init__(self)
        # Inicia a UI criada no Qt Designer
        self.setupUi(self)
		
    def setGameName(self, gameName):
        self.gameName.setText(gameName)
		
    def setGamePrice(self, gamePrice):
        self.gamePrice.setText(gamePrice)
		
    def setGameInfo(self, gameInfo):
        self.gameInfo.setText(gameInfo)
        
    def setGameList(self, gameList):
        lm = ListModel(gameList, self)
        self.gameList.setModel(lm)
        
class ListModel(QAbstractListModel): 
    def __init__(self, datain, parent=None, *args): 
        """ datain: a list where each item is a row
        """
        QAbstractListModel.__init__(self, parent, *args) 
        self.listdata = datain
 
    def rowCount(self, parent=QModelIndex()): 
        return len(self.listdata) 
 
    def data(self, index, role): 
        if index.isValid() and role == Qt.DisplayRole:
            return QVariant(self.listdata[index.row()])
        else: 
            return QVariant()
