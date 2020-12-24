import sys

from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import config

class Black(QWidget):
    """
    General room class
    """
    def __init__(self,time=1000):
        super().__init__()
        self.left = 0
        self.top = 0
        self.width = 1080
        self.height = 860
        self.image_height = 810

        self.time = time

        self.initUI()

    def initUI(self):
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.setBackground()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.lightsOff)
        self.timer.start(self.time)

    def setBackground(self):
        # Add paint widget and paint
        self.m = PaintWidget(self)
        self.m.move(0,0)
        self.m.resize(self.width,self.height)
        
    def lightsOff(self):
        self.timer.stop()
        self.close()

class FatalError(Black):
    super().__init__()

    def initUI(self):
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.setBackground()

        # Close Button
        

        # Second Chance Button

class PaintWidget(QWidget):
    def paintEvent(self, event):
        qp = QPainter(self)
        
        qp.setPen(QPen(Qt.black,5,Qt.SolidLine))
        qp.setBrush(QBrush(Qt.black,Qt.SolidPattern))
        qp.drawRect(0,0,1080,860)

