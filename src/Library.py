# importing libraries 
import sys 

from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 

from Room import Room
from Entry import Entry
from Balcony import Balcony
import Kitchen
import config

class Library(Room):
    """
    Kitchen window to pop up when player navigates to the Kitchen Location
    """
    def __init__(self):
        super().__init__("Library") 
        # Calling the user interface function

        # Setting up buttons and other room windows
        self.livingButton = QPushButton("Living Room", self)
        self.livingButton.setGeometry(self.width/2-self.button_width/2,self.image_height-self.button_height,self.button_width,self.button_height)
        self.livingButton.clicked.connect(self.toLiving)

        self.ey = None
        self.entryButton = QPushButton("Entry", self)
        self.entryButton.setGeometry(self.width-self.button_width,self.height/2-self.button_height,100,50)
        self.entryButton.clicked.connect(self.toEntry)

        self.ki = None
        self.kitchenButton = QPushButton("Kitchen", self)
        self.kitchenButton.setGeometry(self.left,self.image_height/2-self.button_height/2,self.button_width,self.button_height)
        self.kitchenButton.clicked.connect(self.toKitchen)

    def toLiving(self, checked):
        self.close()

    def toEntry(self, checked):
        if self.ey is None:
            self.ey = Entry()
            self.ey.show()
        else:
            self.ey.close()
            self.ey = None

    def toKitchen(self, checked):
        if self.ki is None:
            self.ki = Kitchen.Kitchen()
            self.ki.show()
            self.close()
        else:
            self.ki.close()
            self.ki = None