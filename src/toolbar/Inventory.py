import sys

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QPushButton
from PyQt5.QtGui import QPainter, QColor, QPen, QIcon, QBrush, QPixmap
from PyQt5.QtCore import Qt

import config

class Inventory(QWidget):
    """
    General room class
    """
    def __init__(self):
        super().__init__()
        self.title = "Inventory"
        self.left = 480
        self.top = 0
        self.width = 600
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)