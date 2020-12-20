import sys

import json
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout, QListView, QLineEdit
from PyQt5.QtGui import QPainter, QColor, QPen, QIcon, QBrush, QPixmap, QImage
from PyQt5.QtCore import Qt, QAbstractListModel

import config

class ContactList(QAbstractListModel):
    def __init__(self, *args, contacts=[], **kwargs):
        super(ContactList, self).__init__(*args, **kwargs)
        self.contacts = contacts

    def data(self, index, role):
        if role == Qt.DisplayRole:
            text = self.contacts[index.row()]
            return text

    def rowCount(self, index):
        return len(self.contacts)

class Phone(QWidget):
    """
    General room class
    """
    def __init__(self):
        super().__init__()
        self.title = "Phone"

        self.left = 440
        self.top = 300
        self.width = 200
        self.height = 300

        self.save_dir = "../data/save_files/"

        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)

        self.service = QLabel(f"Service: {config.progress.service_status}", self)
        self.service.move(150,100)
        self.contactView = QListView()
        self.callButton = QPushButton(text="Call")
        self.callButton.pressed.connect(self.call)

        self.model = ContactList(contacts=["Ned","Mom","Dad"])
        self.contactView.setModel(self.model)

        self.window_layout = QVBoxLayout() 
        self.window_layout.addWidget(self.service)
        self.window_layout.addWidget(self.contactView)
        self.window_layout.addWidget(self.callButton)
        self.setLayout(self.window_layout)

    def call(self):
        """
        """
        pass
      
        self.show()