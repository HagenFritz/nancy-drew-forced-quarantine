# importing libraries 
import sys 

from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 

from Room import Room
import config

class Laundry(Room):
    """
    Balcony window to pop up when player navigates to the Balcony Location
    """
    def __init__(self):
        super().__init__("Laundry") 
        # Calling the user interface function

        self.setRoomButtons()
        self.setInteractionButtons()
        self.setEasterEggButtons()

    def setRoomButtons(self):
    	# Setting up buttons and other room windows
        self.entryButton = QPushButton("Entry", self)
        self.entryButton.setGeometry(self.width/2-self.button_width/2,self.image_height-self.button_height,self.button_width,self.button_height)
        self.entryButton.clicked.connect(self.toEntry)

    def setInteractionButtons(self):
        # Dryer Setting
        self.settingButton = QPushButton("", self)
        self.settingButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        self.settingButton.setGeometry(360,540,self.bw,self.bh)
        self.settingButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.settingButton.clicked.connect(self.toSetting) 

        # Dryer Start
        self.startButton = QPushButton("", self)
        self.startButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        self.startButton.setGeometry(560,540,self.bw,self.bh)
        self.startButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.startButton.clicked.connect(self.toStart) 

        # Litter
        self.litterButton = QPushButton("", self)
        self.litterButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        self.litterButton.setGeometry(425,150,self.bw,self.bh)
        self.litterButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.litterButton.clicked.connect(self.toUnused)

    def setEasterEggButtons(self):
        """
        Setting up easter egg buttons
        """
        # duct
        self.ductButton = QPushButton("", self)
        self.ductButton.setGeometry(610,110,10,10)
        self.ductButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.ductButton.clicked.connect(self.toDuct)

    def toEntry(self, checked):
        self.close()

    def toSetting(self, checked):
        self.playAudio("cant_do",nancy=True)

    def toStart(self, checked):
        self.playAudio("cant_do",nancy=True)

        