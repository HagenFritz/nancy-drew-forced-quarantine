import sys
sys.path.append("../")
import cv2
import json
import numpy as np 
import pandas as pd

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from Room import Room
from LivingRoom import LivingRoom
import config

class StartMenu(QDialog):

    def __init__(self):
        super().__init__()
        self.title = 'Menu'
        self.left = 0
        self.top = 0
        self.width = 480
        self.height = 650

        self.game  = None
        self.menu = None
        self.load_game = None 
        self.leader_board_window = None

        self.f_size = 28
        self.button_width = 340
        self.button_height = 80

        self.setBackground()
        self.setButtons()
        self.initUI()
        
    def initUI(self):  

        self.nancy_title = QLabel("Nancy Drew", self)
        self.nancy_title.setStyleSheet("color: gold; background-color: black; qproperty-alignment: 'AlignHCenter | AlignVCenter'; border-width: 2px; border-color: black; font: bold 28px;")
        self.nancy_title.setGeometry(50,50,380,50)
        self.game_title = QLabel("Forced Quarantine", self)
        self.game_title.setStyleSheet("color: gold; background-color: black; qproperty-alignment: 'AlignHCenter | AlignVCenter'; border-width: 2px; border-color: black; font: bold 44px;") 
        self.game_title.setGeometry(50,90,380,50)   

        self.exitButton = QPushButton('Exit', self)
        self.exitButton.setGeometry((self.width - self.button_width)/2,500,self.button_width,self.button_height)
        self.exitButton.setStyleSheet(f"color: black; background-color: white; border-width: 2px; border-color: black; font: bold {self.f_size}px;")
        self.exitButton.clicked.connect(self.toExit)

    def setButtons(self):
       
        self.startButton = QPushButton('Start New Game', self)
        self.startButton.setGeometry((self.width - self.button_width)/2,170,self.button_width,self.button_height)
        self.startButton.setStyleSheet(f"color: black; background-color: white; border-width: 2px; border-color: black; font: bold {self.f_size}px;")
        self.startButton.clicked.connect(self.toGame)

        self.loadButton = QPushButton('Load Game', self)
        self.loadButton.setGeometry((self.width - self.button_width)/2,280,self.button_width,self.button_height)
        self.loadButton.setStyleSheet(f"color: black; background-color: white; border-width: 2px; border-color: black; font: bold {self.f_size}px;")
        self.loadButton.clicked.connect(self.toLoad)

        self.leaderButton = QPushButton('Leaderboard', self)
        self.leaderButton.setGeometry((self.width - self.button_width)/2,390,self.button_width,self.button_height)
        self.leaderButton.setStyleSheet(f"color: black; background-color: white; border-width: 2px; border-color: black; font: bold {self.f_size}px;")
        self.leaderButton.clicked.connect(self.toLeader)

    def toGame(self, checked):
        if self.game is None:
            self.game = LivingRoom()
            self.game.show()
            self.close()
        else:
            self.game.close()
            self.game = None

        self.close()

    def toOldGame(self, checked):
        # play start video
        # Create a VideoCapture object and read from input file 
        cap = cv2.VideoCapture('../videos/test.mp4') 
        cap.set(3, 1080)
        cap.set(4, 860)
           
        # Check if camera opened successfully 
        if (cap.isOpened()== False):  
            print("Error opening video file") 
           
        # Read until video is completed 
        while(cap.isOpened()): 
              
            # Resize frame
            ret, frame = cap.read() 
            width = int(frame.shape[1] * 2.25)
            height = int(frame.shape[0] * 3.17)
            dim = (width, height)
            frame =  cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)
            # Capture frame-by-frame 
            if ret == True: 
           
                # Display the resulting frame
                cv2.imshow('Frame', frame) 
           
                # Press Q on keyboard to  exit 
                if cv2.waitKey(25) & 0xFF == ord('q'): 
                    break
           
            # Break the loop 
            else:  
                break
           
        # When everything done, release  
        # the video capture object 
        cap.release() 
           
        # Closes all the frames 
        cv2.destroyAllWindows()
        # creates first window
        if self.game is None:
            self.game = LivingRoom()
            self.game.show()
            self.close()
        else:
            self.game.close()
            self.game = None

    def toLoad(self, checked):
        if self.load_game is None:
            self.load_game = LoadGame()
            self.load_game.show()
            self.close
        else:
            self.load_game.close()
            self.load_game = None

    def toLeader(self, checked):
        if self.leader_board_window is None:
            self.leader_board_window = Leaderboard()
            self.leader_board_window.show()
            self.close
        else:
            self.leader_board_window.close()
            self.leader_board_window = None

    def toMenu(self, checked):
        if self.menu is None:
            self.menu = StartMenu()
            self.menu.show()
            self.close()
        else:
            self.menu.close()
            self.menu = None

    def toExit(self, checked):
        QCoreApplication.exit(0)

    def setBackground(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Add paint widget and paint
        self.m = PaintWidget(self)
        self.m.move(0,0)
        self.m.resize(self.width,self.height)

class LoadGame(StartMenu):

    def __init__(self):
        super().__init__()
        self.title = 'Load Game'

    def setButtons(self):
       
        self.startButton = QPushButton('Choose File', self)
        self.startButton.setGeometry((self.width - self.button_width)/2,170,self.button_width,self.button_height)
        self.startButton.setStyleSheet(f"color: black; background-color: white; border-width: 2px; border-color: black; font: bold {self.f_size}px;")
        self.startButton.clicked.connect(self.toReloadGame)

        self.leaderButton = QPushButton('Back to Menu', self)
        self.leaderButton.setGeometry((self.width - self.button_width)/2,390,self.button_width,self.button_height)
        self.leaderButton.setStyleSheet(f"color: black; background-color: white; border-width: 2px; border-color: black; font: bold {self.f_size}px;")
        self.leaderButton.clicked.connect(self.toMenu)

    def toReloadGame(self, checked):
        fname = self.openFileNameDialog()
        try:
            with open(fname, "r") as f:
                saved_data = json.load(f)
                print("File loaded succesfully!")
        except Exception as inst:
            print(f"Problem loading save file - {inst}")
            sys.exit(1)

        try:
            config.progress.data = pd.DataFrame.from_dict(saved_data["progress"])
            config.progress.notes = saved_data["notes"]
            config.nancy.inventory = saved_data["inventory"]
        except Exception as inst:
            print(f"Problem loading in data - {inst}")
            sys.exit(1)

        if self.game is None:
            self.game = LivingRoom()
            self.game.show()
            self.close()
        else:
            self.game.close()
            self.game = None

        self.close()

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fname, _ = QFileDialog.getOpenFileName(self,"Choose File", "../data/save_files","JSON Files (*.json)")
        return fname

class Leaderboard(StartMenu):

    def __init__(self):
        super().__init__()
        self.title = 'Leaderboard'

        self.setLeaders()

    def setButtons(self):

        self.leaderButton = QPushButton('Back to Menu', self)
        self.leaderButton.setGeometry((self.width - self.button_width)/2,390,self.button_width,self.button_height)
        self.leaderButton.setStyleSheet(f"color: black; background-color: white; border-width: 2px; border-color: black; font: bold {self.f_size}px;")
        self.leaderButton.clicked.connect(self.toMenu)

    def setLeaders(self):

        leaders = pd.read_csv("../data/leaders.csv")
        for i in range(3):
            name = leaders.iloc[i,0]
            score = leaders.iloc[i,1]
            self.leader = QLabel(f"{name}\t\t\t{score}", self)
            self.leader.setGeometry((self.width - self.button_width)/2,180+50*i,self.button_width,50)
            self.leader.setStyleSheet("color: white; background-color: black; font: 24px; qproperty-alignment: 'AlignHCenter | AlignVCenter';")

class PaintWidget(QWidget):
    def paintEvent(self, event):
        qp = QPainter(self)
        
        qp.setPen(QPen(Qt.black,5,Qt.SolidLine))
        qp.setBrush(QBrush(Qt.black,Qt.SolidPattern))
        qp.drawRect(0,0,480,850)

