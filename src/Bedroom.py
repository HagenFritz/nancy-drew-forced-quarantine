# importing libraries 
import sys 

from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 

import Hallway
from Room import Room
from Alarm import Alarm
import config

class Bedroom(Room):
    """
    Bedroom window to pop up when player navigates to the Bedroom Location
    """
    def __init__(self):
        super().__init__("Bedroom")
        # Calling the user interface function
        self.setRoomButtons()
        self.setInteractionButtons()
        self.setEasterEggButtons()

    def setRoomButtons(self):
        # Setting up buttons and other room windows
        self.hw = None
        self.hallwayButton = QPushButton("Hallway", self)
        self.hallwayButton.setGeometry(self.width/2-self.button_width/2,self.image_height-self.button_height,self.button_width,self.button_height)
        self.hallwayButton.clicked.connect(self.toHallway)

    def setInteractionButtons(self):
        # setting evening buttons
        if config.game_time.isDay() == False:
            # Alarm
            self.alarm_window = None
            self.alarmButton = QPushButton("", self)
            self.alarmButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
            self.alarmButton.setGeometry(502,460,self.bw,self.bh)
            self.alarmButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
            self.alarmButton.clicked.connect(self.toAlarm) 

            # Bedside books
            self.booksButton = QPushButton("", self)
            self.booksButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
            self.booksButton.setGeometry(210,430,self.bw,self.bh)
            self.booksButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
            self.booksButton.clicked.connect(self.toBooks)

            # Bedside Lights - Right
            self.rightLightsButton = QPushButton("", self)
            self.rightLightsButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
            self.rightLightsButton.setGeometry(532,225,self.bw,self.bh)
            self.rightLightsButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
            self.rightLightsButton.clicked.connect(self.toLightsOff)

            # Bedside Lights - Left
            self.leftLightsButton = QPushButton("", self)
            self.leftLightsButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
            self.leftLightsButton.setGeometry(160,263,self.bw,self.bh)
            self.leftLightsButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
            self.leftLightsButton.clicked.connect(self.toLightsOff)
        else:
            # Alarm
            self.alarm_window = None
            self.alarmButton = QPushButton("", self)
            self.alarmButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
            self.alarmButton.setGeometry(475,535,self.bw,self.bh)
            self.alarmButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
            self.alarmButton.clicked.connect(self.toAlarm) 

            # Candle
            self.booksButton = QPushButton("", self)
            self.booksButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
            self.booksButton.setGeometry(105,525,self.bw,self.bh)
            self.booksButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
            self.booksButton.clicked.connect(self.toBooks)

    def setEasterEggButtons(self):
        pass

    def toHallway(self, checked):
        config.progress.rooms_visited += 1
        if self.hw is None:
            self.hw = Hallway.Hallway()
            self.hw.show()
        else:
            self.hw.close()
            self.hw = None
        self.close()

    def toBooks(self, checked):
        self.playAudio("hmm",nancy=True)

    def toAlarm(self, checked):
        if config.progress.data.loc["met_ingman","complete"] == True:
            if self.alarm_window is None:
                self.alarm_window = Alarm()
                self.alarm_window.show()
            else:
                self.alarm_window.close()
                self.alarm_window = None

            self.close()
        else:
            self.playAudio("cant_do",nancy=True)
