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
        self.blenderButton.setGeometry(200,675,self.bw,self.bh)
        self.blenderButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.blenderButton.clicked.connect(self.toSink) 

    def setEasterEggButtons(self):
        pass

    def toHallway(self, checked):
        config.progress.rooms_visited += 1
        self.close()

    def toSink(self, checked):
        self.playAudio("hand_washing",wait=False)