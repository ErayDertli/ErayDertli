
#   Structure of Qt5 GUIS


#eliziçooookkkk seviyorummm

    # imports
import sys
from PyQt5.QtWidgets import QApplication, QWidget   # avoid wild imports
#from PyQt5.QtWidgets import*   # Qwidge modülünün tüm sınıflarını dahil etmek yerine "QApplication" ve "Qwidget" sınıfları dahil edilmelidir.

# Create aplication
app = QApplication(sys.argv)

# Create Window
win = QWidget() 

# Add widgets and change properties
win.setWindowTitle('PyQt5 GUI') # Oluşturulan pencerenin isminin belirlenmesi için.
#win.resize(400,300)     # set window size : with, hight    Oluşturulan pencerenin boyutunun belirlenmesi için kullanılır. Eğer yazılmazsa default seçilir.

# show the constructed
win.show()  

# Execute the application
sys.exit(app.exec_())   #clealy exit on exceptions 
#app.exec()  # Qt exec_ ends with an underscode
#app.exec_() # exec is a Python keyword
