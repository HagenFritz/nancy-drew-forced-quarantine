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

    def setRoomButtons(self):
    	# Setting up buttons and other room windows
        self.balconyButton = QPushButton("Balcony", self)
        self.balconyButton.setGeometry(self.width/2-self.button_width/2,self.image_height-self.button_height,self.button_width,self.button_height)
        self.balconyButton.clicked.connect(self.toBalcony)

    def setInteractionButtons(self):
        # door
        self.doorButton = QPushButton("", self)
        self.doorButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        if config.game_time.isDay():
            self.doorButton.setGeometry(502,580,self.bw,self.bh)
        else:
            self.doorButton.setGeometry(520,580,self.bw,self.bh)
        self.doorButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.doorButton.clicked.connect(self.toLocked) 

        # duct
        self.ductButton = QPushButton("", self)
        self.ductButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        if config.game_time.isDay():
            self.ductButton.setGeometry(640,55,self.bw,self.bh)
        else:
            self.ductButton.setGeometry(690,60,self.bw,self.bh)
        self.ductButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.ductButton.clicked.connect(self.toDuct) 

    def toBalcony(self, checked):
        self.close()

