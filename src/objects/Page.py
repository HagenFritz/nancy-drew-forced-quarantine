import sys
import os

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QPushButton
from PyQt5.QtGui import QPainter, QColor, QPen, QIcon, QBrush, QPixmap
from PyQt5.QtCore import Qt
import sounddevice as sd
import soundfile as sf
from random import randint

from Inventory import Inventory
from Notes import Notes
from Tasks import Tasks
from Phone import Phone
import config

class Page(QWidget):
    """
    General Page window class
    """
    def __init__(self,page_name, page_number):
        super().__init__()
        self.name = page_name
        self.no = page_number
        self.title = f"{self.name}{self.no}"
        self.left = 0
        self.top = 0
        self.width = 620
        self.height = 860
        self.image_height = 810

        self.button_width = 100
        self.button_height = 50
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)

        self.setBackgroundImage()
        self.setToolbarBackground()
        self.setToolbar()

    def setBackgroundImage(self):
        label = QLabel(self)
        pixmap = QPixmap(f'../images/objects/{self.title.lower()}.png')
        label.setPixmap(pixmap)

    def setToolbarBackground(self):
        # Add paint widget and paint
        self.m = PaintWidget(self)
        self.m.move(0,0)
        self.m.resize(self.width,self.height)

    def setToolbar(self):
        # Close
        self.closeButton = QPushButton("Close", self)
        self.closeButton.setGeometry(self.width/2-self.button_width/2,self.image_height,self.button_width,self.button_height)
        self.closeButton.clicked.connect(self.toClose)

        # Next Page
        if os.path.isfile(f"../images/objects/{self.name}{self.no+1}.png"):
            self.next = None
            self.closeButton = QPushButton("Next", self)
            self.closeButton.setGeometry(self.width-self.button_width-10,self.image_height,self.button_width,self.button_height)
            self.closeButton.clicked.connect(self.toNext)

        # Previous Page
        if os.path.isfile(f"../images/objects/{self.name}{self.no-1}.png"):
            self.previous = None
            self.closeButton = QPushButton("Previous", self)
            self.closeButton.setGeometry(10,self.image_height,self.button_width,self.button_height)
            self.closeButton.clicked.connect(self.toPrevious)

    def toClose(self, checked):
        self.close()

    def toNext(self, checked):
        if self.next is None:
            self.next = Page(self.name,self.no+1)
            self.next.show()
        else:
            self.next.close()  # Close window.
            self.next = None  # Discard reference.

        self.close()

    def toPrevious(self, checked):
        if self.previous is None:
            self.previous = Page(self.name,self.no-1)
            self.previous.show()
        else:
            self.previous.close()  # Close window.
            self.previous = None  # Discard reference.
            
        self.close()

class PaintWidget(QWidget):
    def paintEvent(self, event):
        qp = QPainter(self)
        
        qp.setPen(QPen(Qt.black,5,Qt.SolidLine))
        qp.setBrush(QBrush(Qt.black,Qt.SolidPattern))
        qp.drawRect(0, 810, 1080, 50)

