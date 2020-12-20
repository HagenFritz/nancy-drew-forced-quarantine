import sys
sys.path.append("./toolbar/")
sys.path.append("./objects/")

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QPushButton
from PyQt5.QtGui import QPainter, QColor, QPen, QIcon, QBrush, QPixmap
from PyQt5.QtCore import Qt
import sounddevice as sd
import soundfile as sf
from random import randint

import Inventory
from Notes import Notes
from Tasks import Tasks
from Phone import Phone
from Object import Object
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

        self.obj_window = None

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
            self.inventory_window = Inventory.Inventory()
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

    def toNugget(self, checked):
        config.progress.nugget_clicks += 1
        num = randint(0,1)
        if num == 0:
            self.playAudio("cat_meow")
        else:
            self.playAudio("cat_meow_low")

    def toUnused(self, checked):
        self.playAudio("hmm",nancy=True)

    def toLocked(self, checked):
        self.playAudio("locked",nancy=True)

    def toNoSleep(self, checked):
        self.playAudio("no_sleep",nancy=True)

    def grabObject(self, item,):
        if "bag" in config.nancy.inventory or item == "bag":
            if item in config.nancy.inventory:
                self.playAudio("have_that",nancy=True)
            else:
                if self.obj_window is None:
                    config.nancy.inventory.append(item)
                    self.obj_window = Object(item)
                    self.obj_window.show()
                    self.playAudio("got_it",nancy=True)
                else:
                    self.obj_window.close()
                    self.obj_window = None
        else:
            self.playAudio("put_that",nancy=True)

    def lookAtObject(self, item):
        if self.obj_window is None:
            self.obj_window = Object(item)
            self.obj_window.show()
        else:
            self.obj_window.close()
            self.obj_window = None

    def playAudio(self, fname, wait=True, nancy=False):
        """
        Plays audio file
        """
        if nancy:
            filename = f"../audio/nancy/{fname}.wav"
        else:
            filename = f"../audio/{fname}.wav"

        data, fs = sf.read(filename, dtype='float32')  
        sd.play(data, fs)
        if wait:
            status = sd.wait()

class PaintWidget(QWidget):
    def paintEvent(self, event):
        qp = QPainter(self)
        
        qp.setPen(QPen(Qt.black,5,Qt.SolidLine))
        qp.setBrush(QBrush(Qt.black,Qt.SolidPattern))
        qp.drawRect(0, 810, 1080, 50)

