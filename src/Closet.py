# importing libraries 
import sys 

from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 

from Room import Room
import config

class Closet(Room):
    """
    Balcony window to pop up when player navigates to the Balcony Location
    """
    def __init__(self):
        super().__init__("Closet") 
        # Calling the user interface function

        self.setRoomButtons()
        self.setInteractionButtons()

    def setRoomButtons(self):
        """
    	Setting up buttons and other room windows
        """
        self.entryButton = QPushButton("Entry", self)
        self.entryButton.setGeometry(self.width/2-self.button_width/2,self.image_height-self.button_height,self.button_width,self.button_height)
        self.entryButton.clicked.connect(self.toEntry)

    def setInteractionButtons(self):
        # Umbrella
        self.umbrellaButton = QPushButton("", self)
        self.umbrellaButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        self.umbrellaButton.setGeometry(885,650,self.bw,self.bh)
        self.umbrellaButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.umbrellaButton.clicked.connect(self.toUmbrella) 

        # Paper Bag
        self.bagButton = QPushButton("", self)
        self.bagButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        self.bagButton.setGeometry(460,380,self.bw,self.bh)
        self.bagButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.bagButton.clicked.connect(self.toUnused)

    def toEntry(self, checked):
        self.close()

    def toUmbrella(self, checked):
        self.playAudio("cant_do",nancy=True)
