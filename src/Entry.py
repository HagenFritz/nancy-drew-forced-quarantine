# importing libraries 
import sys 
sys.path.append("./interactions/")

from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sounddevice as sd
import soundfile as sf

from Room import Room
from Closet import Closet
from Laundry import Laundry
import config

class Entry(Room):
    """
    Kitchen window to pop up when player navigates to the Kitchen Location
    """
    def __init__(self):
        super().__init__("Entry") 
        # Calling the user interface functions
        self.setRoomButtons()
        self.setInteractionButtons()
        self.setEasterEggButtons()

    def setRoomButtons(self):
    	# Setting up buttons and other room windows
        self.libraryButton = QPushButton("Library", self)
        self.libraryButton.setGeometry(self.width/2-self.button_width/2,self.image_height-self.button_height,self.button_width,self.button_height)
        self.libraryButton.clicked.connect(self.toLibrary)

        # closet
        self.closet = None
        self.closetButton = QPushButton("", self)
        self.closetButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        self.closetButton.setGeometry(self.width-215,self.image_height-130,25,25)
        self.closetButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.closetButton.clicked.connect(self.toCloset)

        # laundry
        self.laundry = None
        self.laundryButton = QPushButton("", self)
        self.laundryButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        self.laundryButton.setGeometry(710,470,25,25)
        self.laundryButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.laundryButton.clicked.connect(self.toLaundry)

    def setInteractionButtons(self):
        # Setting up buttons to interact with
        bw = 25
        bh = 25

        # thermostat
        self.thermostat_window = None
        self.thermostatButton = QPushButton("", self)
        self.thermostatButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        self.thermostatButton.setGeometry(self.width-285,480,bw,bh)
        self.thermostatButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.thermostatButton.clicked.connect(self.toThermostat)

        # front door
        self.frontdoor_window = None
        self.frontDoorButton = QPushButton("", self)
        self.frontDoorButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        self.frontDoorButton.setGeometry(self.width/2+105,self.image_height/2+15,bw,bh)
        self.frontDoorButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.frontDoorButton.clicked.connect(self.toFrontDoor)

        # light switch
        self.light_window = None
        self.lightButton = QPushButton("", self)
        self.lightButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        self.lightButton.setGeometry(360,420,bw,bh)
        self.lightButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.lightButton.clicked.connect(self.toUnused)

    def setEasterEggButtons(self):
        # Setting up easter egg buttons
        # duct
        self.ductButton = QPushButton("", self)
        self.ductButton.setGeometry(self.width/2+220,20,10,10)
        self.ductButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.ductButton.clicked.connect(self.toDuct)

    def toLaundry(self, checked):
        if self.laundry is None:
            self.laundry = Laundry()
            self.laundry.show()
        else:
            self.laundry.close()
            self.laundry = None

    def toCloset(self, checked):
        if self.closet is None:
            self.closet = Closet()
            self.closet.show()
        else:
            self.closet.close()
            self.closet = None

    def toLibrary(self, checked):
        self.close()

    def toThermostat(self, checked):
        pass

    def toFrontDoor(self, checked):
        if config.progress.data.loc["front_unlocked", "complete"] == False:
            filename = "../audio/locked.wav"
            data, fs = sf.read(filename, dtype='float32')  
            sd.play(data, fs)
            status = sd.wait()
        else:
            # need to add something here later
            pass

    def toDuct(self, checked):
        if config.progress.duct_clicked == False:
            config.progress.easter_egg_count += 1
            config.progress.duct_clicked = True
            # audio
            filename = "../audio/cat_meow.wav"
            data, fs = sf.read(filename, dtype='float32')  
            sd.play(data, fs)
            status = sd.wait()