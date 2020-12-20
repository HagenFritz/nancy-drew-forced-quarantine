# importing libraries 
import sys 

from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 

from Room import Room
import config

class Cabinet(Room):
    """
    Balcony window to pop up when player navigates to the Balcony Location
    """
    def __init__(self):
        super().__init__("Cabinet") 
        # Calling the user interface function

        self.setRoomButtons()
        self.setInteractionButtons()
        self.setEasterEggButtons()

    def setRoomButtons(self):
    	# Setting up buttons and other room windows
        self.kitchenButton = QPushButton("Kitchen", self)
        self.kitchenButton.setGeometry(self.width/2-self.button_width/2,self.image_height-self.button_height,self.button_width,self.button_height)
        self.kitchenButton.clicked.connect(self.toKitchen)

    def setInteractionButtons(self):
        bw = 25
        bh = 25

        # Coffee Beans
        self.beansButton = QPushButton("", self)
        self.beansButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        self.beansButton.setGeometry(288,695,bw,bh)
        self.beansButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.beansButton.clicked.connect(self.toBeans)

        # Chemex
        self.chemexButton = QPushButton("", self)
        self.chemexButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        self.chemexButton.setGeometry(565,545,bw,bh)
        self.chemexButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.chemexButton.clicked.connect(self.toChemex)

        # Filters
        self.filterButton = QPushButton("", self)
        self.filterButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        self.filterButton.setGeometry(170,650,bw,bh)
        self.filterButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.filterButton.clicked.connect(self.toFilters)

        # Frother
        self.frotherButton = QPushButton("", self)
        self.frotherButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        self.frotherButton.setGeometry(735,545,bw,bh)
        self.frotherButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.frotherButton.clicked.connect(self.toUnused)

    def setEasterEggButtons(self):
        # Mixed
        self.mixerButton = QPushButton("", self)
        self.mixerButton.setGeometry(458,765,10,10)
        self.mixerButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.mixerButton.clicked.connect(self.toMixer)

    def toKitchen(self, checked):
        self.close()

    def toBeans(self, checked):
        self.grabObject("beans")

    def toChemex(self, checked):
        # need image
        self.grabObject("chemex")

    def toFilters(self, checked):
        # need image
        self.grabObject("filters")

    def toMixer(self, checked):
        if config.progress.mixer_clicked == False:
            config.progress.easter_egg_count += 1
            config.progress.mixer_clicked = True
            self.playAudio("mixer")