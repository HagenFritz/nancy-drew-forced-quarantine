from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QPushButton
from PyQt5.QtGui import QPainter, QColor, QPen, QIcon, QBrush, QPixmap
from PyQt5.QtCore import Qt

import Character
import config

class Interaction(QWidget):
    """
    General room class
    """
    def __init__(self,interaction_name):
        super().__init__()
        self.title = interaction_name
        self.left = 0
        self.top = 0
        self.width = 1080
        self.height = 860
        self.image_height = 810
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)

class CharacterInteraction(QWidget):

    def __init__(self, Character):
        super().__init__()
        self.title = Character.name

        self.left = 0
        self.top = 0
        self.width = 500
        self.height = 860
        self.image_height = 720
        self.text_height = 200

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)

        self.setBackgroundImage()
        self.setTextBackground()

    def setBackgroundImage(self):
        label = QLabel(self)
        if config.game_time.isDay():
            pixmap = QPixmap(f"../images/characters/{self.title.lower()}_day.png")
            label.setPixmap(pixmap)
        else:
            pixmap = QPixmap(f"../images/characters/{self.title.lower()}_night.png")
            label.setPixmap(pixmap)

    def setTextBackground(self):
        # Add paint widget and paint
        self.m = PaintWidget(self)
        self.m.move(0,0)
        self.m.resize(self.width,self.height)

class MessageInteraction(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "Message"
        self.number = config.progress.message_no

        self.left = 0
        self.top = 0
        self.width = 612
        self.height = 792

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        config.progress.first_message = True

class PaintWidget(QWidget):
    def paintEvent(self, event):
        qp = QPainter(self)
        left = 0
        top = 600
        width = 500
        height = 255
        # Character response window
        c_window_height = 75
        qp.setPen(QPen(Qt.white,5,Qt.SolidLine))
        qp.setBrush(QBrush(Qt.black,Qt.SolidPattern))
        qp.drawRect(left, top, width, c_window_height)
        # Player response window
        p_window_height = height - c_window_height
        qp.setPen(QPen(Qt.white,5,Qt.SolidLine))
        qp.setBrush(QBrush(Qt.black,Qt.SolidPattern))
        qp.drawRect(left, top + c_window_height, width, p_window_height)

