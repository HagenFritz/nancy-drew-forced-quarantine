# importing libraries 
import sys 

from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 

from Room import Room
import config

class Bathroom(Room):
    """
    Kitchen window to pop up when player navigates to the Kitchen Location
    """
    def __init__(self):
        super().__init__("Bathroom") 
        # Calling the user interface function

        # Setting up buttons for other rooms
        self.livingButton = QPushButton("Living Room", self)
        self.livingButton.setGeometry(670,810,100,50)
        self.livingButton.clicked.connect(self.toLiving)

    def toLiving(self, checked):
        self.close()