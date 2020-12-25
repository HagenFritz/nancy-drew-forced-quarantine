# importing libraries 
import sys 

from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 

from Room import Room
import config

class Laptop(Room):
    """
    Laptop window to pop up when player navigates to laptop window
    """
    def __init__(self):
        super().__init__("Laptop") 

        self.setRoomButtons()
        self.setInteractionButtons()

    def setRoomButtons(self):
    	# Setting up buttons and other room windows
        self.studyButton = QPushButton("Study", self)
        self.studyButton.setGeometry(self.width/2-self.button_width/2,self.image_height-self.button_height,self.button_width,self.button_height)
        self.studyButton.clicked.connect(self.toStudy)

    def setInteractionButtons(self):
        # might not need this
        bw = 25
        bh = 25

    def toStudy(self, checked):
        """
        Exits the laptop window
        """
        self.close()


