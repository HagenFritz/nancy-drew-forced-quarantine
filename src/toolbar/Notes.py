import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import config

class NotesList(QAbstractListModel):
    def __init__(self, *args, **kwargs):
        super(InventoryList, self).__init__(*args, **kwargs)
        self.notes = config.progress.getNotes()
        print(self.objects)

    def data(self, index, role):
        if role == Qt.DisplayRole:
            text = self.notes[index.row()]
            return text

    def rowCount(self, index):
        return len(self.notes)

class Notes(QWidget):
    """
    General room class
    """
    def __init__(self):
        super().__init__()
        self.title = "Notes"
        self.left = 115
        self.top = 450
        self.width = 300
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)

        