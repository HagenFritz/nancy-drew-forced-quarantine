# importing libraries 
import sys 
sys.path.append("./interactions/")

from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sounddevice as sd
import soundfile as sf

from Room import Room
from Library import Library
from Study import Study
from Cabinet import Cabinet
from Cutting import Cutting
from Interaction import MessageInteraction
import config

class Kitchen(Room):
    """
    Kitchen window to pop up when player navigates to the Kitchen Location
    """
    def __init__(self):
        if config.progress.message == True:
            super().__init__("Kitchen","message")
        else:
            super().__init__("Kitchen")

        self.setRoomButtons()
        self.setInteractionButtons()
        self.setEasterEggButtons()

    def setRoomButtons(self):
        # Setting up buttons for other room
        self.livingButton = QPushButton("Living Room", self)
        self.livingButton.setGeometry(self.width/2-self.button_width/2,self.image_height-self.button_height,self.button_width,self.button_height)
        self.livingButton.clicked.connect(self.toLiving)

        self.ly = None
        self.libraryButton = QPushButton("Library", self)
        self.libraryButton.setGeometry(self.width-self.button_width,self.image_height/2-self.button_height/2,100,50)
        self.libraryButton.clicked.connect(self.toLibrary)

        self.sy = None
        self.studyButton = QPushButton("Study", self)
        self.studyButton.setGeometry(self.left,self.image_height/2-self.button_height/2,self.button_width,self.button_height)
        self.studyButton.clicked.connect(self.toStudy)

        # Coffee Cabinet
        self.cabinet = None
        self.cabinetButton = QPushButton("", self)
        self.cabinetButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        self.cabinetButton.setGeometry(45,245,25,25)
        self.cabinetButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.cabinetButton.clicked.connect(self.toCabinet) 

        # Cutting Board
        self.cutting_window = None
        self.cuttingButton = QPushButton("", self)
        self.cuttingButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        self.cuttingButton.setGeometry(155,385,25,25)
        self.cuttingButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.cuttingButton.clicked.connect(self.toCutting) 

    def setInteractionButtons(self):
        # Setting up buttons to interact with
        bw = 25
        bh = 25
        # Fruit
        self.fruitButton = QPushButton("", self)
        self.fruitButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        self.fruitButton.setGeometry(320,535,bw,bh)
        self.fruitButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.fruitButton.clicked.connect(self.toUnused) 

        # Blender
        self.blenderButton = QPushButton("", self)
        self.blenderButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        self.blenderButton.setGeometry(112,350,bw,bh)
        self.blenderButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.blenderButton.clicked.connect(self.toBlender) 

        # Grinder
        self.grinderButton = QPushButton("", self)
        self.grinderButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        self.grinderButton.setGeometry(150,355,bw,bh)
        self.grinderButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.grinderButton.clicked.connect(self.toGrinder) 

        # Hidden buttons
        self.message_window = None
        self.messageButton = QPushButton("", self)
        self.messageButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        self.messageButton.setGeometry(935,350,bw,bh)
        self.messageButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.messageButton.clicked.connect(self.toMessage) 
        self.messageButton.hide()

        if config.progress.message == True:
            self.messageButton.show()

    def setEasterEggButtons(self):
        # Setting up easter egg buttons
        # pans
        # griddle
        self.griddleButton = QPushButton("", self)
        self.griddleButton.setGeometry(400,200,10,10)
        self.griddleButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.griddleButton.clicked.connect(self.toGriddle)

        # frying
        self.fryingButton = QPushButton("", self)
        self.fryingButton.setGeometry(205,225,10,10)
        self.fryingButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.fryingButton.clicked.connect(self.toFrying)

        # sauce
        self.sauceButton = QPushButton("", self)
        self.sauceButton.setGeometry(65,215,10,10)
        self.sauceButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.sauceButton.clicked.connect(self.toSauce)

        # pancake
        self.pancakeButton = QPushButton("", self)
        self.pancakeButton.setGeometry(120,150,10,10)
        self.pancakeButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.pancakeButton.clicked.connect(self.toPancake)

        # stock
        self.stockButton = QPushButton("", self)
        self.stockButton.setGeometry(295,75,10,10)
        self.stockButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.stockButton.clicked.connect(self.toStock)

        # wok
        self.wokButton = QPushButton("", self)
        self.wokButton.setGeometry(540,120,10,10)
        self.wokButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.wokButton.clicked.connect(self.toWok)

        # pot
        self.potButton = QPushButton("", self)
        self.potButton.setGeometry(585,75,10,10)
        self.potButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.potButton.clicked.connect(self.toPot)

        # coffee
        self.babyButton = QPushButton("", self)
        self.babyButton.setGeometry(470,140,10,10)
        self.babyButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.babyButton.clicked.connect(self.toBaby)

    def toLiving(self, checked):
        config.progress.rooms_visited += 1
        self.close()

    def toLibrary(self, checked):
        config.progress.rooms_visited += 1
        if self.ly is None:
            self.ly = Library()
            self.ly.show()
        else:
            self.ly.close()
            self.ly = None

    def toStudy(self, checked):
        config.progress.rooms_visited += 1
        if self.sy is None:
            self.sy = Study()
            self.sy.show()
        else:
            self.sy.close()
            self.sy = None

    def toCabinet(self, checked):
        if self.cabinet is None:
            self.cabinet = Cabinet()
            self.cabinet.show()
        else:
            self.cabinet.close()
            self.cabinet = None

    def toCutting(self, checked):
        if self.cutting_window is None:
            self.cutting_window = Cutting()
            self.cutting_window.show()
        else:
            self.cutting_window.close()
            self.cutting_window = None

    def toBlender(self, checked):
        self.playAudio("blender")

    def toGrinder(self, checked):
        if "beans" in config.nancy.inventory:
            self.playAudio("grinding")
            config.nancy.inventory.append("grounds")
        else:
            self.playAudio("missing_something")

    def toMessage(self, checked):
        if self.message_window is None and config.progress.message == True:
            self.message_window = MessageInteraction()
            self.message_window.show()
        else:
            self.message_window.close()
            self.message_window = None

    def toGriddle(self, checked):
        playAudio("griddle")
        config.progress.pan_orchestra += 1

    def toFrying(self, checked):
        playAudio("frying")
        config.progress.pan_orchestra += 1

    def toSauce(self, checked):
        playAudio("sauce")
        config.progress.pan_orchestra += 1

    def toPancake(self, checked):
        playAudio("pancake")
        config.progress.pan_orchestra += 1

    def toStock(self, checked):
        playAudio("stock")
        config.progress.pan_orchestra += 1

    def toWok(self,checked):
        playAudio("wok")
        config.progress.pan_orchestra += 1

    def toPot(self,checked):
        playAudio("pot")
        config.progress.pan_orchestra += 1

    def toBaby(self,checked):
        self.playAudtio("coffee")
        config.progress.pan_orchestra += 1
