# importing libraries 
import sys 

from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 

from Room import Room
import config

class Bathroom(Room):
    """
    Kitchen window to pop up when player navigates to the Kitchen Location
    """
    def __init__(self):
        super().__init__("Bathroom") 
        # Calling the user interface function
        self.setRoomButtons()
        self.setInteractionButtons()
        self.setEasterEggButtons()

    def setRoomButtons(self):
        # Setting up buttons and other room windows
        self.hallwayButton = QPushButton("Hallway", self)
        self.hallwayButton.setGeometry(self.width/2-self.button_width/2,self.image_height-self.button_height,self.button_width,self.button_height)
        self.hallwayButton.clicked.connect(self.toHallway)

    def setInteractionButtons(self):
        # Sink
        self.blenderButton = QPushButton("", self)
        self.blenderButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        self.blenderButton.setGeometry(310,575,self.bw,self.bh)
        self.blenderButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.blenderButton.clicked.connect(self.toSink) 

        # Drawer
        self.drawerButton = QPushButton("", self)
        self.drawerButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        self.drawerButton.setGeometry(857,585,self.bw,self.bh)
        self.drawerButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.drawerButton.clicked.connect(self.toLocked) 

        # Cabinet
        self.cabinetButton = QPushButton("", self)
        self.cabinetButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        self.cabinetButton.setGeometry(773,665,self.bw,self.bh)
        self.cabinetButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.cabinetButton.clicked.connect(self.toLocked) 

        # Toilet Paper
        self.toiletPaperButton = QPushButton("", self)
        self.toiletPaperButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        self.toiletPaperButton.setGeometry(1010,690,self.bw,self.bh)
        self.toiletPaperButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.toiletPaperButton.clicked.connect(self.toToiletPaper)

    def setEasterEggButtons(self):
        pass

    def toHallway(self, checked):
        config.progress.rooms_visited += 1
        self.close()

    def toSink(self, checked):
        self.playAudio("hand_washing",wait=False)

    def toToiletPaper(self, checked):
        self.grabObject("toilet paper")