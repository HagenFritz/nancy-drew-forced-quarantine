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
        self.setRoomButtons()
        self.setInteractionButtons()
        self.setEasterEggButtons()

    def setRoomButtons(self):
        # Setting up buttons and other room windows
        self.kitchenButton = QPushButton("Kitchen", self)
        self.kitchenButton.setGeometry(self.width/2-self.button_width/2,self.image_height-self.button_height,self.button_width,self.button_height)
        self.kitchenButton.clicked.connect(self.toKitchen)

    def setInteractionButtons(self):
        # Setting up buttons to interact with
        bw = 25
        bh = 25



        # Nugget
        self.nuggetButton = QPushButton("", self)
        self.nuggetButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        self.nuggetButton.setGeometry(960,425,bw,bh)
        self.nuggetButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.nuggetButton.clicked.connect(self.toNugget) 

        # Daybed
        self.daybed = QPushButton("", self)
        self.daybed.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        self.daybed.setGeometry(800,500,bw,bh)
        self.daybed.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.daybed.clicked.connect(self.toNoSleep) 

        # Left Daybed Drawer
        self.leftDaybed = QPushButton("", self)
        self.leftDaybed.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        self.leftDaybed.setGeometry(655,600,bw,bh)
        self.leftDaybed.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.leftDaybed.clicked.connect(self.toLocked) 

        # Right Daybed Drawer
        self.leftDaybed = QPushButton("", self)
        self.leftDaybed.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        self.leftDaybed.setGeometry(735,705,bw,bh)
        self.leftDaybed.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.leftDaybed.clicked.connect(self.toLocked) 

        # Cactus
        self.cactusButton = QPushButton("", self)
        self.cactusButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        self.cactusButton.setGeometry(610,350,bw,bh)
        self.cactusButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.cactusButton.clicked.connect(self.toUnused) 

        # Big Light
        self.bigLightButton = QPushButton("", self)
        self.bigLightButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        self.bigLightButton.setGeometry(765,140,bw,bh)
        self.bigLightButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.bigLightButton.clicked.connect(self.toUnused)

        # Little Light 
        self.lilLightButton = QPushButton("", self)
        self.lilLightButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        self.lilLightButton.setGeometry(145,265,bw,bh)
        self.lilLightButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.lilLightButton.clicked.connect(self.toUnused)

    def setEasterEggButtons(self):
        # Setting up easter egg buttons
        # UFO
        self.ufoButton = QPushButton("", self)
        self.ufoButton.setGeometry(637,185,10,10)
        self.ufoButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        #self.ufoButton.clicked.connect(self.toUFO)

    def toKitchen(self, checked):
    	self.close()