# importing libraries 
import sys 

from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 

from Room import Room
from Chairs import Chairs
from Vent import Vent
import config

class Balcony(Room):
    """
    Balcony window to pop up when player navigates to the Balcony Location
    """
    def __init__(self):
        super().__init__("Balcony") 
        # Calling the user interface function

        self.setRoomButtons()
        self.setInteractionButtons()
        self.setEasterEggButtons()

    def setRoomButtons(self):
    	# Setting up buttons and other room windows
        self.livingButton = QPushButton("Living Room", self)
        self.livingButton.setGeometry(self.width/2-self.button_width/2,self.image_height-self.button_height,self.button_width,self.button_height)
        self.livingButton.clicked.connect(self.toLiving)

        self.chairs = None
        self.chairsButton = QPushButton("Right", self)
        self.chairsButton.setGeometry(self.width-self.button_width,self.image_height/2-self.button_height/2,100,50)
        self.chairsButton.clicked.connect(self.toChairs)

        self.vent = None
        self.ventButton = QPushButton("Left", self)
        self.ventButton.setGeometry(self.left,self.image_height/2-self.button_height/2,self.button_width,self.button_height)
        self.ventButton.clicked.connect(self.toVent)

    def setInteractionButtons(self):
        pass

    def setEasterEggButtons(self):
        pass

    def toChairs(self, checked):
        if self.chairs is None:
            self.chairs = Chairs()
            self.chairs.show()
        else:
            self.chairs.close()
            self.chairs = None

    def toVent(self, checked):
        if self.vent is None:
            self.vent = Vent()
            self.vent.show()
        else:
            self.vent.close()
            self.vent = None

    def toLiving(self, checked):
        self.close()