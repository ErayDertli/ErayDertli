import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction

from PyQt5.QtGui import *
from PyQt5 import QtGui

class GUI(QMainWindow):                                                                                                  # inherit from QMainWindow
    def __init__(self) :
        super().__init__()                                                                                               # initialize super class, which creates the Window

        self.initUI()

    def initUI(self):          
        # set properties and add widgets 
        self.setWindowTitle('PyQt GUI')     
        self.resize(400, 500)        
        self.add_menus_and_status()                                                                                     # writing in the status bar (Pencerenin altındaki mesaj kutusu)

    def add_menus_and_status(self) :        
        self.statusBar().showMessage('Text in Status Bar') 
        menubar = self.menuBar()                                                                                         # Create menu bar 
         
        file_menu = menubar.addMenu('File')                                                                              # writing in the menu bar
        ###############################################################################################################################################################
        #new_icon = QtGui.QIcon()
        # new_icon.addPixmap(QtGui.QPixmap(".\\icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)                          # Firma kodlarından icon uygulamasına örnek
        #self.setWindowIcon(new_icon)
        ###############################################################################################################################################################   

        new_icon = QIcon('C:/Users/engin/Desktop/Embedded Sofware_Processes/2_Programs/1_ConfToll/1_Tests/icon.png')
        new_action = QAction(new_icon,'New', self)
        new_action.setStatusTip('New File')     
        file_menu.addAction(new_action)

        file_menu.addSeparator()

        exit_icon = QIcon('C:/Users/engin/Desktop/Embedded Sofware_Processes/2_Programs/1_ConfToll/1_Tests/exit_icon.png')
        exit_action = QAction(exit_icon, 'Exit', self)
        exit_action.setStatusTip('Click to the application') 
        exit_action.triggered.connect(self.close)    
        exit_action.setShortcut('Ctrl+Q')                           # Yapacağı işlemin kısa yol tuşu belirtiliyor
        file_menu.addAction(exit_action)
        
        edit_menu = menubar.addMenu('Edit')
           
        


if __name__ == '__main__' :
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec_())
