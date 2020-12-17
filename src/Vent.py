# importing libraries 
import sys 

from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 

from Room import Room
import config

class Vent(Room):
    """
    Balcony window to pop up when player navigates to the Balcony Location
    """
    def __init__(self):
        super().__init__("Vent") 
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
        pass

    def setEasterEggButtons(self):
        pass

    def toBalcony(self, checked):
        self.close()