import sys
sys.path.append("./toolbar/")
sys.path.append("./objects/")
import json

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sounddevice as sd
import soundfile as sf
from random import randint

from Inventory import Inventory
from Notes import Notes
from Tasks import Tasks
from Phone import Phone
from Object import Object
from Page import Page
from Screen import Black
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

        # room button properties
        self.button_width = 100
        self.button_height = 50
        # interaction button properties
        self.bw = 25
        self.bh = 25

        self.obj_window = None
        self.page_window = None
        self.black_window = None

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

        self.save_window = None
        self.saveButton = QPushButton("Save", self)
        self.saveButton.setGeometry(self.width-5-self.button_width-spacing*1,self.image_height,self.button_width,self.button_height)
        self.saveButton.clicked.connect(self.toSave)

        self.exitButton = QPushButton("Exit", self)
        self.exitButton.setGeometry(self.width-5-self.button_width-spacing*0,self.image_height,self.button_width,self.button_height)
        self.exitButton.clicked.connect(self.toExit)

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

    def toSave(self, checked):
        """
        Saves current data
        """
        fname = self.getText()
        # progress as csv
        save_dict = {"progress":config.progress.data.to_dict(),"inventory":config.nancy.inventory,"notes":config.progress.notes}
        try:
            with open(f"../data/save_files/{fname}.json", "w") as f:
                data = json.dump(save_dict, f)
            
            save_status_text = "Save Successful!"
        except Exception as inst:
            print("Error -", inst)

            save_status_text = "Save Unsuccessful"

        saveStatus = QMessageBox.information(self, 'Save Game', save_status_text, QMessageBox.Ok, QMessageBox.Ok)

    def toExit(self, checked):
        """
        Exits game
        """
        checkExit = QMessageBox.question(self, 'Exit Game', "Are you sure?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if checkExit == QMessageBox.Yes:
            sys.exit(0)
        else:
            pass

    def getText(self):
        text, okPressed = QInputDialog.getText(self, "Save Game","File Name:", QLineEdit.Normal, "")
        if okPressed and text != '':
            return text

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

    def toDuct(self, checked):
        config.progress.duct_checked += 1
        self.playAudio("cat_meow")

    def toLightsOff(self,checked):
        if config.game_time.isDay() == False: # only works if at night
            config.progress.lights_switched += 1
            if self.black_window is None:
                self.black_window = Black()
                self.black_window.show()
            else:
                self.black_window.close()
                self.black_window = None
        else:
            self.playAudio("hmm")

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

    def readPage(self, page_name):
        if self.page_window is None:
            self.page_window = Page(page_name,1)
            self.page_window.show()
        else:
            self.page_window.close()
            self.page_window = None

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

