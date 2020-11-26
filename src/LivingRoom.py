# importing libraries 
import sys 
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

class LivingRoom(Room):
    """

    """

    def __init__(self):
        super().__init__("Living Room")
        self.setGeometry(self.left,self.top,self.width,self.height)

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

