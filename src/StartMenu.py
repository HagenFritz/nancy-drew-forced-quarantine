import sys
import cv2 
import numpy as np 

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon, QPalette, QColor
from PyQt5.QtCore import pyqtSlot, QCoreApplication

from Room import Room
from LivingRoom import LivingRoom

class StartMenu(QDialog):

    def __init__(self):
        super().__init__()
        self.title = 'Menu'
        self.left = 0
        self.top = 0
        self.width = 1080
        self.height = 860
        self.game  = None
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.createGridLayout()
    
    def createGridLayout(self):

        layout = QVBoxLayout()
        
        self.startButton = QPushButton('Start New Game')
        self.startButton.clicked.connect(self.toGame)
        layout.addWidget(self.startButton)

        self.loadButton = QPushButton('Load Game')
        self.loadButton.clicked.connect(self.toLoad)
        layout.addWidget(self.loadButton)

        self.leaderButton = QPushButton('Leaderboard')
        self.leaderButton.clicked.connect(self.toLeader)
        layout.addWidget(self.leaderButton)

        self.exitButton = QPushButton('Exit')
        self.exitButton.clicked.connect(self.toExit)
        layout.addWidget(self.exitButton)

        self.setLayout(layout)

    def toGame(self, checked):
        # play start video
        # Create a VideoCapture object and read from input file 
        cap = cv2.VideoCapture('../videos/test.mp4') 
           
        # Check if camera opened successfully 
        if (cap.isOpened()== False):  
            print("Error opening video file") 
           
        # Read until video is completed 
        while(cap.isOpened()): 
              
            # Capture frame-by-frame 
            ret, frame = cap.read() 
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