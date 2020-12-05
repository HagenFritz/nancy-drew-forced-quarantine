# importing libraries 
import sys 
sys.path.append("./interactions/")
from random import randint

from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 

import config
from Room import Room
from Balcony import Balcony
from Kitchen import Kitchen
from Hallway import Hallway
from Library import Library
import sounddevice as sd
import soundfile as sf

from IngmanSpeaking import IngmanSpeaking

class LivingRoom(Room):
    """

    """

    def __init__(self):
        super().__init__("Living Room")
        self.setGeometry(self.left,self.top,self.width,self.height)

        self.setRoomButtons()
        self.setInteractionButtons()
        self.setEasterEggButtons()

    def setRoomButtons(self):
        # Setting up buttons and other room windows
        self.by = None
        self.balconyButton = QPushButton("Balcony", self)
        self.balconyButton.setGeometry(self.left,self.image_height/2-self.button_height/2,self.button_width,self.button_height)
        self.balconyButton.clicked.connect(self.toBalcony)

        self.hw = None
        self.hallwayButton = QPushButton("Hallway", self)
        self.hallwayButton.setGeometry(self.width/2-self.button_width/2,self.image_height-self.button_height,self.button_width,self.button_height)
        self.hallwayButton.clicked.connect(self.toHallway) 

        self.ly = None
        self.libraryButton = QPushButton("Library", self)
        self.libraryButton.setGeometry(self.width-self.button_width,self.image_height/2-self.button_height/2,100,50)
        self.libraryButton.clicked.connect(self.toLibrary) 

    def setInteractionButtons(self):
        # Setting up buttons to interact with
        # Dr. Ingman
        bw = 25
        bh = 25
        self.ingman_window = None
        self.ingmanButton = QPushButton("", self)
        self.ingmanButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        self.ingmanButton.setGeometry(500,450,bw,bh)
        self.ingmanButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.ingmanButton.clicked.connect(self.toIngman) 

        # Nugget
        self.nuggetButton = QPushButton("", self)
        self.nuggetButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        self.nuggetButton.setGeometry(930,560,bw,bh)
        self.nuggetButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.nuggetButton.clicked.connect(self.toNugget) 

        # Books
        self.booksButton = QPushButton("", self)
        self.booksButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        self.booksButton.setGeometry(360,515,bw,bh)
        self.booksButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.booksButton.clicked.connect(self.toBooks) 

        # Controllers
        self.controllersButton = QPushButton("", self)
        self.controllersButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        self.controllersButton.setGeometry(590,560,bw,bh)
        self.controllersButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.controllersButton.clicked.connect(self.toControllers)

        # Lamp
        self.lampButton = QPushButton("", self)
        self.lampButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        self.lampButton.setGeometry(305,380,bw,bh)
        self.lampButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.lampButton.clicked.connect(self.toUnused)

        # Light Switch
        self.lightButton = QPushButton("", self)
        self.lightButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        self.lightButton.setGeometry(745,340,bw,bh)
        self.lightButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.lightButton.clicked.connect(self.toLight)

    def setEasterEggButtons(self):
        # Setting up easter egg buttons
        # UFO
        self.ufoButton = QPushButton("", self)
        self.ufoButton.setGeometry(637,185,10,10)
        self.ufoButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.ufoButton.clicked.connect(self.toUFO)

    def toBalcony(self, checked):
        if self.by is None:
            self.by = Balcony()
            self.by.show()
        else:
            self.by.close()
            self.by = None

    def toHallway(self, checked):
        if self.hw is None:
            self.hw = Hallway()
            self.hw.show()
        else:
            self.hw.close()
            self.hw = None

    def toLibrary(self, checked):
        if self.ly is None:
            self.ly = Library()
            self.ly.show()
        else:
            self.ly.close()
            self.ly = None

    def toIngman(self, checked):
        if self.ingman_window is None:
            self.ingman_window = IngmanSpeaking()
            self.ingman_window.show()
        else:
            self.ingman_window.close()
            self.ingman_window = None

    def toNugget(self, checked):
        num = randint(0,1)
        if num == 0:
            filename = "../audio/cat_meow.wav"
        else:
            filename = "../audio/cat_meow_low.wav"
        # Extract data and sampling rate from file
        data, fs = sf.read(filename, dtype='float32')  
        sd.play(data, fs)
        status = sd.wait()  # Wait until file is done playing

    def toBooks(self, checked):
        pass

    def toControllers(self, checked):
        pass

    def toUFO(self, checked):
        if config.progress.ufo_clicked == False:
            config.progress.easter_egg_count += 1
            config.progress.ufo_clicked = True
            filename = "../audio/cat_meow.wav"

            data, fs = sf.read(filename, dtype='float32')  
            sd.play(data, fs)
            status = sd.wait()

    def toLight(self, checked):
        pass

