import sys
sys.path.append("./toolbar/")

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QPushButton
from PyQt5.QtGui import QPainter, QColor, QPen, QIcon, QBrush, QPixmap
from PyQt5.QtCore import Qt
import sounddevice as sd
import soundfile as sf

from Inventory import Inventory
from Notes import Notes
from Tasks import Tasks
from Phone import Phone
import config

class Room(QWidget):
    """
    General room class
    """
    def __init__(self,room_name,bg_image=""):
        super().__init__()
        self.title = room_name
        self.bg_image = bg_image
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
        label = QLabel(self)
        if len(self.bg_image) > 1:
            pixmap = QPixmap(f'../images/rooms/{self.title.lower()}_{self.bg_image}.png')
            label.setPixmap(pixmap)
        else:
            if config.game_time.isDay():
                pixmap = QPixmap(f'../images/rooms/{self.title.lower()}_day.png')
                label.setPixmap(pixmap)
            else:
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
        if self.inventory_window is None:
            self.inventory_window = Inventory()
            self.inventory_window.show()
        else:
            self.inventory_window.close()
            self.inventory_window = None

    def toNotes(self, checked):
        if self.notes_window is None:
            self.notes_window = Notes()
            self.notes_window.show()
        else:
            self.notes_window.close()
            self.notes_window = None

    def toTasks(self, checked):
        if self.tasks_window is None:
            self.tasks_window = Tasks()
            self.tasks_window.show()
        else:
            self.tasks_window.close()
            self.tasks_window = None

    def toPhone(self, checked):
        if self.phone_window is None:
            self.phone_window = Phone()
            self.phone_window.show()
        else:
            self.phone_window.close()
            self.phone_window = None

    def toUnused(self, checked):
        filename = "../audio/hmm.wav"
        data, fs = sf.read(filename, dtype='float32')  
        sd.play(data, fs)
        status = sd.wait()


class PaintWidget(QWidget):
    def paintEvent(self, event):
        qp = QPainter(self)
        
        qp.setPen(QPen(Qt.black,5,Qt.SolidLine))
        qp.setBrush(QBrush(Qt.black,Qt.SolidPattern))
        qp.drawRect(0, 810, 1080, 50)

