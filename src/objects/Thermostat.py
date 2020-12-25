# importing libraries 
import sys 

from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 

from Room import Room
import config

class Thermostat(Room):
    """
    Laptop window to pop up when player navigates to laptop window
    """
    def __init__(self):
        super().__init__("Thermostat") 

        self.setRoomButtons()
        self.setInteractionButtons()

    def setRoomButtons(self):
    	# Setting up buttons and other room windows
        self.studyButton = QPushButton("Entry", self)
        self.studyButton.setGeometry(self.width/2-self.button_width/2,self.image_height-self.button_height,self.button_width,self.button_height)
        self.studyButton.clicked.connect(self.toEntry)

    def setInteractionButtons(self):
        # might not need this
        bw = 25
        bh = 25
        # Plus
        self.morningButton = QPushButton("", self)
        self.morningButton.setGeometry(710,245,100,150)
        self.morningButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.morningButton.clicked.connect(self.toPlus)

        # Minus
        self.morningButton = QPushButton("", self)
        self.morningButton.setGeometry(710,410,100,140)
        self.morningButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.morningButton.clicked.connect(self.toMinus)

    def toEntry(self, checked):
        """
        Exits the laptop window
        """
        self.close()

    def toPlus(self, checked):
        """
        Increases the temperature setpoint
        """
        config.progress.setpoint += 1
        self.playAudio("click")

    def toMinus(self, checked):
        """
        Decreases the temperature setpoint
        """
        config.progress.setpoint -= 1
        self.playAudio("click")

