from asyncio import base_futures
import sys

from PyQt5.QtWidgets import QApplication,QMainWindow, QAction, QWidget
from PyQt5.Qt import QLabel, QPushButton,QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QIcon

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('PyQt5 GUI')
        self.resize(400,300)
        self.add_menus_and_status()
        
        self.horizontal_vertical_box_layout()
        
    def horizontal_vertical_box_layout(self):
        label_1 = QLabel('Firt Label')
        label_2 = QLabel('Another Label')
        
        button_1 = QPushButton('click 1')
        button_2 = QPushButton('click 2')
        
        hbox_1 = QHBoxLayout()
        hbox_2 = QHBoxLayout()
        
        hbox_1.addWidget(label_1)
        hbox_1.addWidget(button_1)
        
        hbox_2.addWidget(label_1)
        hbox_2.addWidget(button_2)
        
        vbox = QVBoxLayout()
        vbox.addLayout(hbox_1)
        vbox.addLayout(hbox_2)
                
        layout_widget = QWidget()
        layout_widget.setLayout(vbox)
        
        self.setCentralWidget(layout_widget)
        
    def add_menus_and_status(self) :        
        self.statusBar().showMessage('Text in Status Bar') 
        menubar = self.menuBar()                                                                                         # Create menu bar 
         
        file_menu = menubar.addMenu('File')                                                                              # writing in the menu bar
        ###############################################################################################################################################################
        #new_icon = QtGui.QIcon()
        # new_icon.addPixmap(QtGui.QPixmap(".\\icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)                          # Firma kodlarýndan icon uygulamasýna örnek
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
        exit_action.setShortcut('Ctrl+Q')                           # Yapacaðý iþlemin kýsa yol tuþu belirtiliyor
        file_menu.addAction(exit_action)
        
        edit_menu = menubar.addMenu('Edit')
           
        


if __name__ == '__main__' :
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec_())