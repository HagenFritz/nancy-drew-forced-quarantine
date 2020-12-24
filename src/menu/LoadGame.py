import sys
import cv2 
import numpy as np 

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from Room import Room
from LivingRoom import LivingRoom
import config

class LoadGame(StartMenu):

    def __init__(self):
        super().__init__()
        self.title = 'Load Game'

        self.menu = None
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.setBackground()

        self.nancy_title = QLabel("Nancy Drew", self)
        self.nancy_title.setStyleSheet("color: gold; background-color: black; qproperty-alignment: 'AlignHCenter | AlignVCenter'; border-width: 2px; border-color: black; font: bold 28px;")
        self.nancy_title.setGeometry(50,50,380,50)
        self.game_title = QLabel("Forced Quarantine", self)
        self.game_title.setStyleSheet("color: gold; background-color: black; qproperty-alignment: 'AlignHCenter | AlignVCenter'; border-width: 2px; border-color: black; font: bold 44px;") 
        self.game_title.setGeometry(50,90,380,50)      
       
        self.startButton = QPushButton('Choose File', self)
        self.startButton.setGeometry(50,170,380,100)
        self.startButton.setStyleSheet("color: black; background-color: white; border-width: 2px; border-color: black; font: bold 32px;")
        self.startButton.clicked.connect(self.toReloadGame)

        #self.loadButton = QPushButton('Saved Game 2', self)
        #self.loadButton.setGeometry(50,280,380,100)
        #self.loadButton.setStyleSheet("color: black; background-color: white; border-width: 2px; border-color: black; font: bold 32px;")
        #self.loadButton.clicked.connect(self.toReloadGame)

        self.leaderButton = QPushButton('Back to Menu', self)
        self.leaderButton.setGeometry(50,390,380,100)
        self.leaderButton.setStyleSheet("color: black; background-color: white; border-width: 2px; border-color: black; font: bold 32px;")
        self.leaderButton.clicked.connect(self.toMenu)

        self.exitButton = QPushButton('Exit', self)
        self.exitButton.setGeometry(50,500,380,100)
        self.exitButton.setStyleSheet("color: black; background-color: white; border-width: 2px; border-color: black; font: bold 32px;")
        self.exitButton.clicked.connect(self.toExit)

    def toReloadGame(self, checked):
        fname = self.openFileNameDialog()
        try:
            saved_data = json.load(fname)
            # loading data into correct files
            config.progress.data = pd.DataFrame.from_dict(saved_data["progress"])
            config.progress.notes = saved_data["notes"]
            config.nancy.inventory = saved_data["inventory"]

            print(saved_data)
        except Exception as inst:
            print(inst)

        if self.game is None:
            self.game = LivingRoom()
            self.game.show()
            self.close()
        else:
            self.game.close()
            self.game = None

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fname, _ = QFileDialog.getOpenFileName(self,"Choose File", "../data/save_files","JSON Files (*.json)")
        return fname

    def toMenu(self, checked):
        if self.menu is None:
            self.menu = StartMenu()
            self.menu.show()
            self.close()
        else:
            self.menu.close()
            self.menu = None

