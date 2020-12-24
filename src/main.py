# importing libraries 
import sys 
sys.path.append("./menu/")
from random import randint

from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 

from StartMenu import StartMenu
from LivingRoom import LivingRoom
from Room import Room

if __name__ == '__main__':
    # create pyqt5 app 
    App = QApplication(sys.argv) 
      
    # create the instance of our Window 
    menu = StartMenu()
    menu.show()
     
    #game = LivingRoom()
    #game.show()

    # start the app 
    sys.exit(App.exec()) 