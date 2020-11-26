from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QPushButton
from PyQt5.QtGui import QPainter, QColor, QPen, QIcon, QBrush, QPixmap
from PyQt5.QtCore import Qt

import config

class Room(QWidget):
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

        self.button_width = 100
        self.button_height = 50
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)

        self.setBackgroundImage()
        self.setToolbarBackground()
        self.setToolbar()

    def setToolbarBackground(self):
        # Add paint widget and paint
        self.m = PaintWidget(self)
        self.m.move(0,0)
        self.m.resize(self.width,self.height)

    def setBackgroundImage(self):
        print('setting image')
        # Create widget
        label = QLabel(self)
        #if config.game_time.isDay():
         #   pixmap = QPixmap(f'{self.title.lower()}_day.pdf')
        #    label.setPixmap(pixmap)
        #else:
        pixmap = QPixmap(f'../images/rooms/{self.title.lower()}_night.png')
        label.setPixmap(pixmap)

    def setToolbar(self):
        spacing = 105
        self.inventory_window = None
        self.inventoryButton = QPushButton("Inventory", self)
        self.inventoryButton.setGeometry(5+spacing*0,self.image_height,self.button_width,self.button_height)
        self.inventoryButton.clicked.connect(self.toInventory)

        self.notes_window = None
        self.notesButton = QPushButton("Notes", self)
        self.notesButton.setGeometry(5+spacing*1,self.image_height,self.button_width,self.button_height)
        self.notesButton.clicked.connect(self.toNotes)

        self.tasks_window = None
        self.tasksButton = QPushButton("Task List", self)
        self.tasksButton.setGeometry(5+spacing*2,self.image_height,self.button_width,self.button_height)
        self.tasksButton.clicked.connect(self.toTasks)

        self.phone_window = None
        self.phoneButton = QPushButton("Phone", self)
        self.phoneButton.setGeometry(5+spacing*3,self.image_height,self.button_width,self.button_height)
        self.phoneButton.clicked.connect(self.toPhone)

    def toInventory(self, checked):
        pass

    def toNotes(self, checked):
        pass

    def toTasks(self, checked):
        pass

    def toPhone(self, checked):
        pass

class PaintWidget(QWidget):
    def paintEvent(self, event):
        qp = QPainter(self)
        
        qp.setPen(QPen(Qt.black,5,Qt.SolidLine))
        qp.setBrush(QBrush(Qt.black,Qt.SolidPattern))
        qp.drawRect(0, 810, 1080, 50)

