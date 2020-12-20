# importing libraries 
import sys 
sys.path.append("./objects/")

from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sounddevice as sd
import soundfile as sf

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

        # Laptop
        self.laptop_window = None
        self.laptopButton = QPushButton("", self)
        self.laptopButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        self.laptopButton.setGeometry(145,540,bw,bh)
        self.laptopButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.laptopButton.clicked.connect(self.toLaptop)

        # Objects
        # RPi
        self.rpiButton = QPushButton("", self)
        self.rpiButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        self.rpiButton.setGeometry(275,435,bw,bh)
        self.rpiButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.rpiButton.clicked.connect(self.toRPiPopup)

        # Coffee Mug
        self.mugButton = QPushButton("", self)
        self.mugButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        self.mugButton.setGeometry(170,460,bw,bh)
        self.mugButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.mugButton.clicked.connect(self.toMugPopup)

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
        self.leftDaybed.setGeometry(745,705,bw,bh)
        self.leftDaybed.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.leftDaybed.clicked.connect(self.toLocked) 

        # Cactus
        self.cactusButton = QPushButton("", self)
        self.cactusButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        self.cactusButton.setGeometry(620,350,bw,bh)
        self.cactusButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.cactusButton.clicked.connect(self.toUnused) 

        # Big Light
        self.bigLightButton = QPushButton("", self)
        self.bigLightButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        self.bigLightButton.setGeometry(775,140,bw,bh)
        self.bigLightButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.bigLightButton.clicked.connect(self.toUnused)

        # Little Light 
        self.lilLightButton = QPushButton("", self)
        self.lilLightButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        self.lilLightButton.setGeometry(145,275,bw,bh)
        self.lilLightButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.lilLightButton.clicked.connect(self.toUnused)

    def setEasterEggButtons(self):
        # Setting up easter egg buttons
        # Frisbee
        self.frisbeeButton = QPushButton("", self)
        self.frisbeeButton.setGeometry(830,80,10,10)
        self.frisbeeButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.frisbeeButton.clicked.connect(self.toFrisbee)

    def toKitchen(self, checked):
        config.progress.rooms_visited += 1
        self.close()

    def toLaptop(self, checked):
        if self.laptop_window is None:
            pass
            #self.laptop_window = Laptop()
            self.laptop_window.show()
        else:
            self.laptop_window.close()
            self.laptop_window = None

    def toMugPopup(self, checked):
        self.grabObject("mug")

    def toRPiPopup(self, checked):
        self.grabObject("rpi")

    def toFrisbee(self, checked):
        if config.progress.frisbee_clicked == False:
            config.progress.easter_egg_count += 1
            config.progress.frisbee_clicked = True
            filename = "../audio/cat_meow.wav" # update with correct sound
            data, fs = sf.read(filename, dtype='float32')  
            sd.play(data, fs)
            status = sd.wait()
