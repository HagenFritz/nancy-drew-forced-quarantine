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
        self.f = self.speakToIngman
        self.nid = 1

        # Meeting Ingman
        if config.progress.data.loc["met_ingman", "complete"] == False:
            # setting current progress step to True and unlocking next task
            config.progress.data.loc["met_ingman", "complete"] = True
            config.progress.data.loc["apt_explored", "visible"] = True

            self.c = self.conversation.firstConversation(self)
        # Explored Apt
        elif config.progress.data.loc["met_ingman", "complete"] == True and config.progress.rooms_visited >= 7 and config.progress.data.loc["apt_explored", "complete"] == False:
            config.progress.data.loc["apt_explored", "complete"] = True
            config.progress.data.loc["make_coffee", "visible"] = True

            self.c = self.conversation.coffeeConversation(self)
        # Made Coffee
        elif config.progress.data.loc["apt_explored", "complete"] == True and config.progress.isCoffeeMade() and config.progress.data.loc["make_coffee","complete"] == False:
            if config.progress.isCoffeeGood() == False:
                self.c = self.conversation.badCoffee(self)
                # changing coffee made flag to false 
                config.progress.coffeeIsMade(False)
                # adding mug back to inventory
                config.nancy.inventory.append("mug")
            else:
                # setting current progress step to True and unlocking next task
                config.progress.data.loc["make_coffee","complete"] = True
                config.progress.data.loc["first_sleep","visible"] = True
                # resetting coffee made flags for future use
                config.progress.coffeeIsMade(False)
                config.progress.coffeeIsGood(False)

                self.c = self.conversation.goodCoffee(self)
        elif config.progress.message == True and config.progress.message_no == 1 and config.progress.message_read == True:
            self.c = self.conversation.noUpdates(self)
        else:
            self.c = self.conversation.noUpdates(self)

        self.f(self.nid)

    def speakToIngman(self, node_id_number):
        """
        Audio code "fc"
        """
        # printing out Ingman answer
        self.answer = QLabel(self.c.get_node(self.nid).data["answer"], self)
        self.answer.setWordWrap(True)
        self.answer.setGeometry(10,605,480,65)
        self.answer.show()
        self.answer.setStyleSheet("color: white; qproperty-alignment: 'AlignLeft | AlignVCenter';")
        self.playResponse(self.c.get_node(self.nid).data["audio"])

        # exiting if no more choices and setting the progress forward
        if self.c.children(self.nid) == []:
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
        try:
            self.secondChoiceButton.clicked.connect(self.secondChoiceAnswer)
        except AttributeError:
            pass

        try:
            self.thirdChoiceButton.clicked.connect(self.thirdChoiceAnswer)
        except AttributeError:
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
        try: 
            self.secondChoiceButton.hide()
        except AttributeError as inst:
            pass

        try:
            self.thirdChoiceButton.hide()
        except AttributeError as inst:
            pass

    def playResponse(self, filename):
        data, fs = sf.read(f"../audio/ingman/{filename}.wav", dtype='float32')  
        sd.play(data, fs)
        status = sd.wait()

