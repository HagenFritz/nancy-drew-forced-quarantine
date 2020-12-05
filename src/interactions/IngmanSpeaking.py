import sys
sys.path.append("./interactions/")

from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sounddevice as sd
import soundfile as sf

from Interaction import CharacterInteraction
from Conversations import Conversations
import config

class IngmanSpeaking(CharacterInteraction):

    def __init__(self):
        super().__init__(config.ingman)
        self.conversation = Conversations

        if config.progress.met_ingman == False:
            self.f = self.meetIngman
            self.nid = 1
            self.c = self.conversation.firstConversation(self)
            self.f(self.nid)
        else:
            self.noUpdates()

    def noUpdates(self):
        '''
        Function to be called if the player hasn't progressed enough to speak further with Ingman
        '''
        pass

    def meetIngman(self, node_id_number):
        """
        Audio code "fc"
        """
        # printing out Ingman answer
        self.answer = QLabel(self.c.get_node(self.nid).data["answer"], self)
        self.answer.move(10,625)
        self.answer.show()
        self.answer.setStyleSheet("color: white")
        self.playResponse(self.c.get_node(self.nid).data["audio"])

        # exiting if no more choices and setting the progress forward
        if self.c.children(self.nid) == []:
            config.progress.met_ingman = True
            self.close()
            
        # printing out your possible responses
        for response in self.c.children(self.nid):
            loc = response.data["loc"]
            if loc == "u":
                self.firstChoiceButton = QPushButton(f"", self)
                self.firstChoiceButton.setText(f"{response.tag}")
                self.firstChoiceButton.show()
                self.firstChoiceButton.setGeometry(0,690,self.width,50)
                self.firstChoiceButton.setStyleSheet("color:white; background-color: rgba(0, 255, 255, 0);")
            elif loc == "d":
                self.secondChoiceButton = QPushButton(f"{response.tag}", self)
                self.secondChoiceButton.show()
                self.secondChoiceButton.setGeometry(0,750,self.width,50)
                self.secondChoiceButton.setStyleSheet("color:white; background-color: rgba(0, 255, 255, 0);")
            else:
                self.thirdChoiceButton = QPushButton(f"{response.tag}", self)
                self.thirdChoiceButton.show()
                self.thirdChoiceButton.setGeometry(0,810,self.width,50)
                self.thirdChoiceButton.setStyleSheet("color:white; background-color: rgba(0, 255, 255, 0);")

        self.firstChoiceButton.clicked.connect(self.firstChoiceAnswer)
        self.secondChoiceButton.clicked.connect(self.secondChoiceAnswer)
        try:
            self.thirdChoiceButton.clicked.connect(self.thirdChoiceAnswer)
        except Exception as inst:
            pass

    def firstChoiceAnswer(self, checked):
        # printing out character's response and getting next question
        for response in self.c.children(self.nid):
            if response.data["loc"] == "u":
                self.nid = response.identifier

        self.destroyButtons()
        self.f(self.nid)

    def secondChoiceAnswer(self, checked):
        # printing out character's response and getting next question
        for response in self.c.children(self.nid):
            if response.data["loc"] == "d":
                self.nid = response.identifier

        self.destroyButtons()
        self.f(self.nid)

    def thirdChoiceAnswer(self, checked):
        # printing out character's response and getting next question
        for response in self.c.children(self.nid):
            if response.data["loc"] == "c":
                self.nid = response.identifier

        self.destroyButtons()
        self.f(self.nid)

    def destroyButtons(self):
        self.answer.hide()
        self.firstChoiceButton.hide()
        self.secondChoiceButton.hide()
        try:
            self.thirdChoiceButton.hide()
        except Exception as inst:
            pass

    def playResponse(self, filename):
        data, fs = sf.read(f"../audio/ingman/{filename}.wav", dtype='float32')  
        sd.play(data, fs)
        status = sd.wait()

