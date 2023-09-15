import sys
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QAction, QWidget
from PyQt5.Qt import QLabel, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon

class GUI(QMainWindow):                                                                                                  # inherit from QMainWindow
    def __init__(self) :
        super().__init__()                                                                                               # initialize super class, which creates the Window
        self.initUI()

    def initUI(self):          
        # set properties and add widgets 
        self.setWindowTitle('PyQt GUI')     
        self.resize(400, 300)        
        self.add_menus_and_status()                                                                                     # writing in the status bar (Pencerenin altındaki mesaj kutusu)

        self.positional_widget_layot()

    def positional_widget_layot(self):
        #label = QLabel('Our Firt Label',self) 
        #label.move (20, 20)                                                                                           #label w/out text, window is the paret 
        label_1 = QLabel('Our Firt Label',self)   
        
        print(self.menuBar().size)
        mbar_height = self.menuBar().height()
        print(mbar_height)
        label_1.move(10, mbar_height)

        label_2 = QLabel('Another Label',self)   
        label_2.move(10, mbar_height*2)

        button_1 = QPushButton('click 1', self)
        button_2 = QPushButton('click 2', self)

        button_1.move(label_1.width(),label_1.height())    
        button_2.move(label_1.width(),label_1.height()*2)    

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
