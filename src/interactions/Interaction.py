from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QPushButton
from PyQt5.QtGui import QPainter, QColor, QPen, QIcon, QBrush, QPixmap
from PyQt5.QtCore import Qt

import config

class Interaction(QWidget):
    """
    General room class
    """
    def __init__(self,room_name):
        super().__init__()
        self.title = room_name
        self.left = 0
        self.top = 0
        self.width = 1080
        self.height = 860
        self.image_height = 810

        #self.button_width = 100
        #self.button_height = 50
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)