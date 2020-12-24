# importing libraries 
import sys 

from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sounddevice as sd
import soundfile as sf

from Room import Room
from Entry import Entry
import Kitchen
import config

class Library(Room):
    """
    Kitchen window to pop up when player navigates to the Kitchen Location
    """
    def __init__(self):
        super().__init__("Library") 
        # Calling the user interface function

        self.setRoomButtons()
        self.setInteractionButtons()
        self.setEasterEggButtons()

    def setRoomButtons(self):
        # Setting up buttons and other room windows
        self.livingButton = QPushButton("Living Room", self)
        self.livingButton.setGeometry(self.width/2-self.button_width/2,self.image_height-self.button_height,self.button_width,self.button_height)
        self.livingButton.clicked.connect(self.toLiving)

        self.ey = None
        self.entryButton = QPushButton("Entry", self)
        self.entryButton.setGeometry(self.width-self.button_width,self.height/2-self.button_height,100,50)
        self.entryButton.clicked.connect(self.toEntry)

        self.ki = None
        self.kitchenButton = QPushButton("Kitchen", self)
        self.kitchenButton.setGeometry(self.left,self.image_height/2-self.button_height/2,self.button_width,self.button_height)
        self.kitchenButton.clicked.connect(self.toKitchen)

    def setInteractionButtons(self):
        bw = 25
        bh = 25
        # Books
        # Dictionary
        self.dictButton = QPushButton("", self)
        self.dictButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        self.dictButton.setGeometry(160,290,bw,bh)
        self.dictButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.dictButton.clicked.connect(self.toDict)

        # Hitchhiker's Guide
        self.dictButton = QPushButton("", self)
        self.dictButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        self.dictButton.setGeometry(270,280,bw,bh)
        self.dictButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.dictButton.clicked.connect(self.toHitchhiker)

        # GOT
        self.dictButton = QPushButton("", self)
        self.dictButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        self.dictButton.setGeometry(180,480,bw,bh)
        self.dictButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.dictButton.clicked.connect(self.toGot)

        # Photography
        self.dictButton = QPushButton("", self)
        self.dictButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        self.dictButton.setGeometry(810,383,bw,bh)
        self.dictButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.dictButton.clicked.connect(self.toPhotobook)

        # Objects
        # Bag
        self.bagButton = QPushButton("", self)
        self.bagButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        self.bagButton.setGeometry(820,280,bw,bh)
        self.bagButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.bagButton.clicked.connect(self.toBag)

        # Locked
        # Top drawer
        self.topButton = QPushButton("", self)
        self.topButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        self.topButton.setGeometry(663,623,bw,bh)
        self.topButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.topButton.clicked.connect(self.toLocked)

        # Middle drawer
        self.midButton = QPushButton("", self)
        self.midButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        self.midButton.setGeometry(663,700,bw,bh)
        self.midButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.midButton.clicked.connect(self.toLocked)

        # Bot Drawer
        self.botButton = QPushButton("", self)
        self.botButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        self.botButton.setGeometry(663,788,bw,bh)
        self.botButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.botButton.clicked.connect(self.toLocked)

        # Lights
        # Switch
        self.lightButton = QPushButton("", self)
        self.lightButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        self.lightButton.setGeometry(3,505,self.bw,self.bh)
        self.lightButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.lightButton.clicked.connect(self.toLightsOff)

        # Unused
        # House
        self.houseButton = QPushButton("", self)
        self.houseButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        self.houseButton.setGeometry(640,510,bw,bh)
        self.houseButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.houseButton.clicked.connect(self.toUnused)

        # Snuff
        self.snuffButton = QPushButton("", self)
        self.snuffButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        self.snuffButton.setGeometry(220,315,bw,bh)
        self.snuffButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.snuffButton.clicked.connect(self.toUnused)

    def setEasterEggButtons(self):
        # Setting up easter egg buttons
        # Tie Fighter
        self.tieButton = QPushButton("", self)
        self.tieButton.setGeometry(310,390,10,10)
        self.tieButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.tieButton.clicked.connect(self.toTie)

        # X Wing
        self.xButton = QPushButton("", self)
        self.xButton.setGeometry(185,390,10,10)
        self.xButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.xButton.clicked.connect(self.toX)

        # Y Wing
        self.yButton = QPushButton("", self)
        self.yButton.setGeometry(270,195,10,10)
        self.yButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.yButton.clicked.connect(self.toY)

    def toLiving(self, checked):
        config.progress.rooms_visited += 1
        self.close()

    def toEntry(self, checked):
        config.progress.rooms_visited += 1
        if self.ey is None:
            self.ey = Entry()
            self.ey.show()
        else:
            self.ey.close()
            self.ey = None

    def toKitchen(self, checked):
        config.progress.rooms_visited += 1
        if self.ki is None:
            self.ki = Kitchen.Kitchen() # typical import is not working
            self.ki.show()
            self.close()
        else:
            self.ki.close()
            self.ki = None

    def toDict(self, checked):
        self.readPage("coffee_brewing")

    def toPhotobook(self, checked):
        # need image
        self.grabObject("photobook")

    def toBag(self, checked):
        # need image
        self.grabObject("bag")

    def toHitchhiker(self, checked):
        # need image
        self.lookAtObject("hitchhiker")

    def toGot(self, checked):
        # need image
        self.readPage("pinout")

    def toTie(self, checked):
        if config.progress.tie_clicked == False:
            config.progress.star_wars_count += 1
            config.progress.tie_clicked = True
            filename = "../audio/tie_fighter.wav"
            data, fs = sf.read(filename, dtype='float32')  
            sd.play(data, fs)
            status = sd.wait()
        else:
            filename = "../audio/hmm.wav"
            data, fs = sf.read(filename, dtype='float32')  
            sd.play(data, fs)
            status = sd.wait()

    def toX(self, checked):
        if config.progress.xwing_clicked == False:
            config.progress.star_wars_count += 1
            config.progress.xwing_clicked = True
            filename = "../audio/xwing.wav"
            data, fs = sf.read(filename, dtype='float32')  
            sd.play(data, fs)
            status = sd.wait()
        else:
            filename = "../audio/hmm.wav"
            data, fs = sf.read(filename, dtype='float32')  
            sd.play(data, fs)
            status = sd.wait()

    def toY(self, checked):
        if config.progress.ywing_clicked == False:
            config.progress.star_wars_count += 1
            config.progress.ywing_clicked = True
            filename = "../audio/ywing.wav"
            data, fs = sf.read(filename, dtype='float32')  
            sd.play(data, fs)
            status = sd.wait()
        else:
            filename = "../audio/hmm.wav"
            data, fs = sf.read(filename, dtype='float32')  
            sd.play(data, fs)
            status = sd.wait()