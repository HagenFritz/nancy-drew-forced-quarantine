import sys
import cv2 
import numpy as np 

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from Room import Room
from LivingRoom import LivingRoom

class StartMenu(QDialog):

    def __init__(self):
        super().__init__()
        self.title = 'Menu'
        self.left = 0
        self.top = 0
        self.width = 480
        self.height = 650

        self.game  = None

        self.initUI()
        
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
       
        self.startButton = QPushButton('Start New Game', self)
        self.startButton.setGeometry(50,170,380,100)
        self.startButton.setStyleSheet("color: black; background-color: white; border-width: 2px; border-color: black; font: bold 32px;")
        self.startButton.clicked.connect(self.toGame)

        self.loadButton = QPushButton('Load Game', self)
        self.loadButton.setGeometry(50,280,380,100)
        self.loadButton.setStyleSheet("color: black; background-color: white; border-width: 2px; border-color: black; font: bold 32px;")
        self.loadButton.clicked.connect(self.toLoad)

        self.leaderButton = QPushButton('Leaderboard', self)
        self.leaderButton.setGeometry(50,390,380,100)
        self.leaderButton.setStyleSheet("color: black; background-color: white; border-width: 2px; border-color: black; font: bold 32px;")
        self.leaderButton.clicked.connect(self.toLeader)

        self.exitButton = QPushButton('Exit', self)
        self.exitButton.setGeometry(50,500,380,100)
        self.exitButton.setStyleSheet("color: black; background-color: white; border-width: 2px; border-color: black; font: bold 32px;")
        self.exitButton.clicked.connect(self.toExit)

    def toGame(self, checked):
        if self.game is None:
            self.game = LivingRoom()
            self.game.show()
            self.close()
        else:
            self.game.close()
            self.game = None

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
        pass

    def toLeader(self, checked):
        pass

    def toExit(self, checked):
        QCoreApplication.exit(0)

    def setBackground(self):
        # Add paint widget and paint
        self.m = PaintWidget(self)
        self.m.move(0,0)
        self.m.resize(self.width,self.height)

class PaintWidget(QWidget):
    def paintEvent(self, event):
        qp = QPainter(self)
        
        qp.setPen(QPen(Qt.black,5,Qt.SolidLine))
        qp.setBrush(QBrush(Qt.black,Qt.SolidPattern))
        qp.drawRect(0,0,480,850)

