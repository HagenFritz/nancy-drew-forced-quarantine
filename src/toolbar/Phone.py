import sys

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QPushButton
from PyQt5.QtGui import QPainter, QColor, QPen, QIcon, QBrush, QPixmap
from PyQt5.QtCore import Qt

import config

class Phone(QWidget):
    """
    General room class
    """
    def __init__(self):
        super().__init__()
        self.title = "Phone"
        self.left = 415
        self.top = 205
        self.width = 300
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)