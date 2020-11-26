# importing libraries 
import sys 

from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 

from Room import Room
from Library import Library
from Study import Study
import config

class Kitchen(Room):
    """
    Kitchen window to pop up when player navigates to the Kitchen Location
    """
    def __init__(self):
        super().__init__("Kitchen") 
        # Calling the user interface function

        # Setting up buttons for other room
        self.livingButton = QPushButton("Living Room", self)
        self.livingButton.setGeometry(670,810,100,50)
        self.livingButton.clicked.connect(self.toLiving)

        self.ly = None
        self.libraryButton = QPushButton("Library", self)
        self.libraryButton.setGeometry(1340,400,100,50)
        self.libraryButton.clicked.connect(self.toLibrary)

        self.sy = None
        self.studyButton = QPushButton("Study", self)
        self.studyButton.setGeometry(0,400,100,50)
        self.studyButton.clicked.connect(self.toStudy)

    def toLiving(self, checked):
        self.close()

    def toLibrary(self, checked):
        if self.ly is None:
            self.ly = Library()
            self.ly.show()
        else:
            self.ly.close()
            self.ly = None

    def toStudy(self, checked):
        if self.sy is None:
            self.sy = Study()
            self.sy.show()
        else:
            self.sy.close()
            self.sy = None