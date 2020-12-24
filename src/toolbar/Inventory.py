import sys

import json
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout, QGridLayout, QListView, QLineEdit
from PyQt5.QtGui import QPainter, QColor, QPen, QIcon, QBrush, QPixmap, QImage
from PyQt5.QtCore import *

import config

class InventoryList(QAbstractListModel):
    def __init__(self, *args, **kwargs):
        super(InventoryList, self).__init__(*args, **kwargs)
        self.objects = config.nancy.getInventory()
        print(self.objects)

    def data(self, index, role):
        if role == Qt.DisplayRole:
            text = self.objects[index.row()]
            return text

    def rowCount(self, index):
        return len(self.objects)

class Inventory(QWidget):
    """
    General room class
    """
    def __init__(self):
        super().__init__()
        self.title = "Inventory"

        self.left = 10
        self.top = 450
        self.width = 300
        self.height = 400

        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)

        self.inventoryView = QListView()
        self.useButton = QPushButton("Use")
        self.useButton.pressed.connect(self.use)
        self.inspectButton = QPushButton("Inspect")
        self.inspectButton.pressed.connect(self.inspect) 

        self.model = InventoryList()
        self.inventoryView.setModel(self.model)

        self.window_layout = QGridLayout()
        self.window_layout.addWidget(self.inventoryView,0,0,3,5)
        self.window_layout.addWidget(self.useButton,4,0,1,2)
        self.window_layout.addWidget(self.inspectButton,4,3,1,2)
        self.setLayout(self.window_layout)
      
        self.show()

    def use(self):
        """
        Interact with items
        """
        pass

    def inspect(self):
        """
        Simply see the items
        """
        pass
