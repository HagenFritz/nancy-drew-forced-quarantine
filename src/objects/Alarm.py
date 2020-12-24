import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sounddevice as sd
import soundfile as sf

from Screen import Black
from Room import Room
import Bedroom
import config

class Alarm(QWidget):
    """
    General Object window class
    """
    def __init__(self):
        super().__init__()
        self.left = 440
        self.top = 300
        self.width = 200
        self.height = 300

        self.setWindowTitle("Alarm")
        self.setGeometry(self.left,self.top,self.width,self.height)

        self.black_window = None
        self.br = None

        self.morning_set = False
        self.evening_set = False

        self.bg_image = "background"
        self.background = QLabel(self)
        pixmap = QPixmap(f'../images/objects/alarm_{self.bg_image}.png')
        self.background.setPixmap(pixmap)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateBackground)
        self.timer.start(500) 

        self.setInteractionButtons()

    def setInteractionButtons(self):
        button_width = 75
        button_height = 30
        # Close
        self.closeButton = QPushButton("Close", self)
        self.closeButton.setGeometry(self.width/2-button_width/2,self.height-button_height,button_width,button_height)
        self.closeButton.clicked.connect(self.toClose) 

        # Morning
        self.morningButton = QPushButton("", self)
        self.morningButton.setGeometry(160,112,35,20)
        self.morningButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.morningButton.clicked.connect(self.toMorning)

        # Evening
        self.eveningButton = QPushButton("", self)
        self.eveningButton.setGeometry(160,162,35,20)
        self.eveningButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.eveningButton.clicked.connect(self.toEvening)
        
    def updateBackground(self):
        """
        Changes background image
        """
        pixmap = QPixmap(f'../images/objects/alarm_{self.bg_image}.png')
        self.background.setPixmap(pixmap)

    def toClose(self, checked):
        if self.morning_set and config.game_time.isDay() == False:
            config.game_time.setTime("day")
            if config.progress.data.loc["first_sleep","complete"] == False:
                config.progress.data.loc["first_sleep","complete"] = True
            # Show new bedroom first
            if self.br is None:
                self.br = Bedroom.Bedroom()
                self.br.show()
            else:
                self.br.close()  # Close window.
                self.br = None  # Discard reference.
            # create black screen over new bedroom
            if self.black_window is None:
                self.black_window = Black()
                self.black_window.show()
            else:
                self.black_window.close()
                self.black_window = None
        elif self.evening_set and config.game_time.isDay() == True:
            config.game_time.setTime("night")
            # Show new bedroom first
            if self.br is None:
                self.br = Bedroom.Bedroom()
                self.br.show()
            else:
                self.br.close()  # Close window.
                self.br = None  # Discard reference.
            # create black screen over new bedroom
            if self.black_window is None:
                self.black_window = Black()
                self.black_window.show()
            else:
                self.black_window.close()
                self.black_window = None
        else:
            filename = f"../audio/nancy/cant_do.wav"
            data, fs = sf.read(filename, dtype='float32')  
            sd.play(data, fs)
            # Reopen bedroom
            self.br = Bedroom.Bedroom()
            self.br.show()


        self.close()

    def toMorning(self, checked):
        """
        Changes alarm background to morning
        """
        if self.morning_set == False:
            self.morning_set = True
            self.bg_image = "morning_set"
        else:
            self.morning_set = False
            self.bg_image = "background"

    def toEvening(self, checked):
        """
        Changes alarm background to evening
        """
        if self.evening_set == False:
            self.evening_set = True
            self.bg_image = "evening_set"
        else:
            self.evening_set = False
            self.bg_image = "background"


