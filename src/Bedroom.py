# importing libraries 
import sys 

from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 

from Room import Room
import config

class Bedroom(Room):
    """
    Bedroom window to pop up when player navigates to the Bedroom Location
    """
    def __init__(self):
        super().__init__("Bedroom")
        # Calling the user interface function
        self.setButtons()

    def setButtons(self):
        # Setting up buttons and other room windows
        self.hallwayButton = QPushButton("Hallway", self)
        self.hallwayButton.setGeometry(self.width/2-self.button_width/2,self.image_height-self.button_height,self.button_width,self.button_height)
        self.hallwayButton.clicked.connect(self.toHallway)

    def toHallway(self, checked):
        self.close()