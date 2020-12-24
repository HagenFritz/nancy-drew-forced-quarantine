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
    def __init__(self):
        super().__init__()

    def initUI(self):
        self.button_width = 150
        self.button_height = 50

        self.setGeometry(self.left,self.top,self.width,self.height)
        self.setBackground()
        self.setMessages()

        # Close Button
        self.closeButton = QPushButton("Close Game", self)
        self.closeButton.setGeometry(self.width/2-self.button_width/2-self.button_width,self.image_height,self.button_width,self.button_height)
        self.closeButton.clicked.connect(self.toClose)

        # Second Chance Button
        self.closeButton = QPushButton("Second Chance", self)
        self.closeButton.setGeometry(self.width/2-self.button_width/2+self.button_width,self.image_height,self.button_width,self.button_height)
        self.closeButton.clicked.connect(self.toSecondChance)

    def setMessages(self):
        """
        Sets the Good/Bad News messages
        """
        # Good News
        text = "You are no longer in quaratine."
        self.writeMessage(f"The Good News: {text}", [100,175,1000,200])

        # Good News
        text = "You are no longer alive."
        self.writeMessage(f"The Bad News: {text}", [100,400,1000,200])

    def writeMessage(self, text, geometry):
        """
        
        """
        self.message = QLabel(f"{text}", self)
        self.message.setWordWrap(True)
        self.message.setGeometry(geometry[0],geometry[1],geometry[2],geometry[3])
        self.message.setStyleSheet("color: gold; qproperty-alignment: 'AlignLeft | AlignVCenter'; font: bold 48px;")
        self.message.show()

    def toClose(self, checked):
        self.config.endGame()

    def toSecondChance(self, checked):
        # Need to add functionality to reset any game problems
        self.close()

class PaintWidget(QWidget):
    def paintEvent(self, event):
        qp = QPainter(self)
        
        qp.setPen(QPen(Qt.black,5,Qt.SolidLine))
        qp.setBrush(QBrush(Qt.black,Qt.SolidPattern))
        qp.drawRect(0,0,1080,860)

