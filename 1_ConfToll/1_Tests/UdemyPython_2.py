
#   Structure of Qt5 GUIS

    # imports
import sys
from PyQt5.QtWidgets import QApplication, QWidget   # avoid wild imports  
#from PyQt5.QtWidgets import*   # Qwidge modülünün tüm sınıflarını dahil etmek yerine "QApplication" ve "Qwidget" sınıfları dahil edilmelidir.

# Create Window
#win = QWidget() 

class GUI (QWidget) :   # interit from QWidget
    def __init__(self): 
        super().__init__()    # initialize super class, which creates the window

        self.initUI()   # refer to window as self
   
    def initUI(self):
        self.setWindowTitle ('PyQt GUI')    # Add widgets and change properties
        self.resize(400,100)
        # Add widgets and change properties
        #win.setWindowTitle('PyQt5 GUI') # Oluşturulan pencerenin isminin belirlenmesi için.
        #win.resize(400,300)     # set window size : with, hight    Oluşturulan pencerenin boyutunun belirlenmesi için kullanılır. Eğer yazılmazsa default seçilir.


    # Create aplication
    #app = QApplication(sys.argv)
if __name__ == '__main__' :
    app = QApplication(sys.argv)    # Create aplication
    gui = GUI()                     # create instance of class
    
        # show the constructed
        #win.show() 
    gui.show()                      # show the constructed PyQt window


        # Execute the application
        #sys.exit(app.exec_())   #clealy exit on exceptions 
        #app.exec()  # Qt exec_ ends with an underscode
        #app.exec_() # exec is a Python keyword
    sys.exit(app.exec())            # Execute the application



