import sys
import json

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout, QListView, QLineEdit
from PyQt5.QtGui import QPainter, QColor, QPen, QIcon, QBrush, QPixmap, QImage
from PyQt5.QtCore import *

import config

tick = QImage("../images/icons/tick.png")

class TaskList(QAbstractListModel):
    def __init__(self, *args, tasks=[], **kwargs):
        super(TaskList, self).__init__(*args, **kwargs)
        self.tasks = tasks

    def data(self, index, role):
        if role == Qt.DisplayRole:
            _, text = self.tasks[index.row()]
            return text

        if role == Qt.DecorationRole:
            status, _ = self.tasks[index.row()]
            if status:
                return tick

    def rowCount(self, index):
        return len(self.tasks)


class Tasks(QWidget):
    """
    General room class
    """
    def __init__(self):
        super().__init__()
        self.title = "Task List"

        self.left = 220
        self.top = 450
        self.width = 300
        self.height = 400

        self.save_dir = "../data/save_files/"

        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)

        self.taskView = QListView()

        df = config.progress.data[config.progress.data["visible"] == 1]
        data = [tuple(r) for r in df[["complete","description"]].to_numpy()]
        self.model = TaskList(tasks=data)
        self.taskView.setModel(self.model)

        self.window_layout = QVBoxLayout() 
        self.window_layout.addWidget(self.taskView)
        self.setLayout(self.window_layout)
      
        self.show()

    def check(self):
        """
        Checks if the task is completed
        """
        indexes = self.taskView.selectedIndexes()
        if indexes:
            index = indexes[0]
            row = index.row()
            status, text = self.model.tasks[row]
            # Change task to true
            self.model.tasks[row] = (True, text)
            # Update list
            self.model.dataChanged.emit(index, index)
            # Clear user selection
            self.taskView.clearSelection()








