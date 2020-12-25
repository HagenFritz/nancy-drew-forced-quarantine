# importing libraries 
import sys 

from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 

from Room import Room
import config

class Chairs(Room):
    """
    Balcony window to pop up when player navigates to the Balcony Location
    """
    def __init__(self):
        super().__init__("Chairs") 
        # Calling the user interface function

        self.setRoomButtons()
        self.setInteractionButtons()
        self.setEasterEggButtons()

    def setRoomButtons(self):
    	# Setting up buttons and other room windows
        self.balconyButton = QPushButton("Balcony", self)
        self.balconyButton.setGeometry(self.width/2-self.button_width/2,self.image_height-self.button_height,self.button_width,self.button_height)
        self.balconyButton.clicked.connect(self.toBalcony)

    def setInteractionButtons(self):
        if config.game_time.isDay():
            # notebook
            self.notebookButton = QPushButton("", self)
            self.notebookButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
            self.notebookButton.setGeometry(510,300,self.bw,self.bh)
            self.notebookButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
            self.notebookButton.clicked.connect(self.toNotebook) 
            # drill
            self.drillButton = QPushButton("", self)
            self.drillButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
            self.drillButton.setGeometry(460,575,self.bw,self.bh)
            self.drillButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
            self.drillButton.clicked.connect(self.toDrill) 
        else:
            # nothing to interact with
            pass

    def setEasterEggButtons(self):
        pass

    def toBalcony(self, checked):
        self.close()

    def toNotebook(self, checked):
        pass

    def toDrill(self, checked):
        self.grabObject("drill")

