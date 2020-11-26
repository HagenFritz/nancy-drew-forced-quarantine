# importing libraries 
import sys 

from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 

from Room import Room
import config

class Study(Room):
    """
    Kitchen window to pop up when player navigates to the Kitchen Location
    """
    def __init__(self):
        super().__init__("Study") 
        # Calling the user interface function

        # Setting up buttons and other room windows
        self.kitchenButton = QPushButton("Library", self)
        self.kitchenButton.setGeometry(670,810,100,50)
        self.kitchenButton.clicked.connect(self.toKitchen)

    def toKitchen(self, checked):
    	self.close()