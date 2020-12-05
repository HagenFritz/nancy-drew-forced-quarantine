import sys

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QPushButton
from PyQt5.QtGui import QPainter, QColor, QPen, QIcon, QBrush, QPixmap
from PyQt5.QtCore import Qt

import config

class Tasks(QWidget):
    """
    General room class
    """
    def __init__(self):
        super().__init__()
        self.title = "Task List"
        self.left = 105
        self.top = 350
        self.width = 400
        self.height = 500
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)