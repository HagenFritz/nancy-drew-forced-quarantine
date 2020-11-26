# importing libraries 
import sys 

from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 

from Room import Room
import config

class Entry(Room):
    """
    Kitchen window to pop up when player navigates to the Kitchen Location
    """
    def __init__(self):
        super().__init__("Entry") 
        # Calling the user interface function

    	# Setting up buttons and other room windows
        self.libraryButton = QPushButton("Library", self)
        self.libraryButton.setGeometry(670,810,100,50)
        self.libraryButton.clicked.connect(self.toLibrary)

    def toLibrary(self, checked):
    	self.close()