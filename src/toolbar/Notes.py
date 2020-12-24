import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import config

class NotesList(QAbstractListModel):
    def __init__(self, *args, **kwargs):
        super(NotesList, self).__init__(*args, **kwargs)
        self.notes = config.progress.getNotes()

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

        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)

        self.notesView = QListView()
        self.closeButton = QPushButton("Close")
        self.closeButton.pressed.connect(self.close)

        self.model = NotesList()
        self.notesView.setModel(self.model)

        self.window_layout = QGridLayout()
        self.window_layout.addWidget(self.notesView,0,0,3,5)
        self.window_layout.addWidget(self.closeButton,4,1,1,3)
        self.setLayout(self.window_layout)
