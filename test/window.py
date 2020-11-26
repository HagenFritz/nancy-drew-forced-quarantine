# importing libraries 
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys 

from Bedroom import Bedroom
  
from random import randint

class Nancy():

    def __init__(self):
        self.name = "Nancy"
        self.item = None

    def setItem(self, item):
        self.item = item

    def hasItem(self):
        if self.item == None:
            return False
        else:
            return True

class Kitchen(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,1000,700)
        global nancy
        layout = QVBoxLayout()
        self.label = QLabel(f"Kitchen")
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.UI()

    def UI(self):
        nancy.setItem("spatula")

class LivingRoom(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bedroom")
        self.setGeometry(0,0,1440,860)
        self.br = None  # No external window yet.
        self.ki = None
        # creating character reference
        global nancy

        self.bedroomButton = QPushButton("Bedroom", self)
        self.bedroomButton.setGeometry(0,0,100,200)

        self.kitchenButton = QPushButton("Kitchen", self)
        self.kitchenButton.setGeometry(300,300,100,200)

        self.UI()

    def UI(self):
        self.bedroomButton.clicked.connect(self.toBedroom)
        self.kitchenButton.clicked.connect(self.toKitchen)

    def toBedroom(self, checked):
        print(f'Nancy has a {nancy.item}')
        if self.br is None:
            self.br = Bedroom()
            self.br.show()
        else:
            self.br.close()  # Close window.
            self.br = None  # Discard reference.

    def toKitchen(self, checked):
        print(f'Nancy has a {nancy.item}')
        if nancy.hasItem() == True:
            if self.ki is None:
                self.ki = Kitchen()
                self.ki.show()
            else:
                self.ki.close()  # Close window.
                self.ki = None  # Discard reference.
  
if __name__ == '__main__':
    # create pyqt5 app 
    App = QApplication(sys.argv) 
      
    # create the instance of our Window 
    nancy = Nancy()
    game = LivingRoom() 
    game.show()
      
    # start the app 
    sys.exit(App.exec()) 