# importing libraries 
import sys 

from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 

from Room import Room
from Bedroom import Bedroom
from Bathroom import Bathroom 
import config

class Hallway(Room):
    """
    Bedroom window to pop up when player navigates to the Bedroom Location
    """
    def __init__(self):
        super().__init__("Hallway")

        self.setRoomButtons()
        self.setInteractionButtons()
        self.setEasterEggButtons()

    def setRoomButtons(self):
        # Setting up buttons and other room windows
        self.livingButton = QPushButton("Living Room", self)
        self.livingButton.setGeometry(self.width/2-self.button_width/2,self.image_height-self.button_height,self.button_width,self.button_height)
        self.livingButton.clicked.connect(self.toLiving)

        self.br = None
        self.bedroomButton = QPushButton("Bedroom", self)
        self.bedroomButton.setGeometry(self.width-self.button_width,self.image_height/2-self.button_height/2,self.button_width,self.button_height)
        self.bedroomButton.clicked.connect(self.toBedroom)

        self.bh = None
        self.bathroomButton = QPushButton("Bathroom", self)
        self.bathroomButton.setGeometry(self.left,self.image_height/2-self.button_height/2,self.button_width,self.button_height)
        self.bathroomButton.clicked.connect(self.toBathroom)

    def setInteractionButtons(self):
        bw = 25
        bh = 25

    def setEasterEggButtons(self):
        # Setting up easter egg buttons
        pass

    def toLiving(self, checked):
        self.close()

    def toBedroom(self, checked):
        if self.br is None:
            self.br = Bedroom()
            self.br.show()
        else:
            self.br.close()  # Close window.
            self.br = None  # Discard reference.

    def toBathroom(self, checked):
        if self.bh is None:
            self.bh = Bathroom()
            self.bh.show()
        else:
            self.bh.close()  # Close window.
            self.bh = None  # Discard reference.
