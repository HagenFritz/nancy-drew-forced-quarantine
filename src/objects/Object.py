import sys

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

class Object(QWidget):
    """
    General Object window class
    """
    def __init__(self,obj_name):
        super().__init__()
        self.title = obj_name
        self.left = 0
        self.top = 0
        self.width = 1080
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
        if config.game_time.isDay():
            pixmap = QPixmap(f'../images/objects/{self.title.lower()}_day.png')
            label.setPixmap(pixmap)
        else:
            pixmap = QPixmap(f'../images/objects/{self.title.lower()}_night.png')
            label.setPixmap(pixmap)

    def setToolbarBackground(self):
        # Add paint widget and paint
        self.m = PaintWidget(self)
        self.m.move(0,0)
        self.m.resize(self.width,self.height)

    def setToolbar(self):
        self.closeButton = QPushButton("Close", self)
        self.closeButton.setGeometry(self.width/2,self.image_height,self.button_width,self.button_height)
        self.closeButton.clicked.connect(self.toClose)

    def toClose(self, checked):
        self.close()

class PaintWidget(QWidget):
    def paintEvent(self, event):
        qp = QPainter(self)
        
        qp.setPen(QPen(Qt.black,5,Qt.SolidLine))
        qp.setBrush(QBrush(Qt.black,Qt.SolidPattern))
        qp.drawRect(0, 810, 1080, 50)

