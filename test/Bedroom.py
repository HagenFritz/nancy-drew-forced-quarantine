# importing libraries 
import sys 
from random import randint

from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 

import config

class Bedroom(QWidget):
    """
    Bedroom window to pop up when player navigates to the Bedroom Location
    """
    def __init__(self):
        super().__init__()
        # initializing the window
        self.setGeometry(0,0,1000,700)
        
        # Calling the user interface function
        self.UI()

    def UI(self):
        config.nancy.setItem("pillow")