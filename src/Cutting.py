# importing libraries 
import sys 

from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 

from Room import Room
import config

class Cutting(Room):
    """
    Balcony window to pop up when player navigates to the Balcony Location
    """
    def __init__(self):
        self.make_coffee = False
        if config.progress.data.loc["apt_explored","complete"] == True and config.progress.data.loc["make_coffee","complete"] == False:
            background_list = []
            for obj in config.nancy.inventory:
                if obj in ["chemex","filters","grounds","mug"]:
                    background_list.append(obj)

            if len(background_list) > 0:
                background_list.sort()
                background_str = ""
                for i, obj in enumerate(background_list):
                    if i == len(background_list)-1:
                        background_str += obj
                    else:
                        background_str = background_str + obj + "_"

                if background_str == "chemex_filters_grounds_mug":
                    self.make_coffee = True
                super().__init__("Cutting",background_str)
            else:
                super().__init__("Cutting","Water") 
        else:
            super().__init__("Cutting","Board") 

        self.setRoomButtons()
        self.setInteractionButtons()
        self.setEasterEggButtons()

        if self.make_coffee:
            self.makeCoffee()

    def setRoomButtons(self):
    	# Setting up buttons and other room windows
        self.kitchenButton = QPushButton("Kitchen", self)
        self.kitchenButton.setGeometry(self.width/2-self.button_width/2,self.image_height-self.button_height,self.button_width,self.button_height)
        self.kitchenButton.clicked.connect(self.toKitchen)

    def setInteractionButtons(self):
        bw = 25
        bh = 25

        # Frother
        self.frotherButton = QPushButton("", self)
        self.frotherButton.setIcon(QIcon("../images/icons/magnifying_glass.png"))
        self.frotherButton.setGeometry(735,545,bw,bh)
        self.frotherButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.frotherButton.clicked.connect(self.toUnused)

    def setEasterEggButtons(self):
        # Mixed
        self.mixerButton = QPushButton("", self)
        self.mixerButton.setGeometry(458,765,10,10)
        self.mixerButton.setStyleSheet("background-color: rgba(0, 255, 255, 0);")
        self.mixerButton.clicked.connect(self.toMixer)

    def toKitchen(self, checked):
        try:
            self.timer.stop()
        except AttributeError:
            # timer was not start because not making coffee
            pass

        self.close()

    def toMixer(self, checked):
        if config.progress.mixer_clicked == False:
            config.progress.easter_egg_count += 1
            config.progress.mixer_clicked = True
            self.playAudio("mixer")

    def makeCoffee(self):
        # Timer to update the page
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateMeasurements)
        self.timer.start(500) 

        # coffee attributes
        self.amt_grounds = 0
        self.amt_water = 0

        txt_w = 100
        txt_h = 30
        self.playAudio("need_measurements",wait=False)

        # grounds
        # -------
        self.groundsInput = QLineEdit(self)
        x = 290
        y = 425
        self.groundsInput.move(x, y)
        self.groundsInput.resize(txt_w,txt_h)
        # label
        self.setUnits(x,y,txt_h,"Tbsp")
        # button
        self.measureGrounds = QPushButton("Add",self)
        self.measureGrounds.setGeometry(x+txt_w,y-2.5,50,txt_h+5)
        self.measureGrounds.clicked.connect(self.addGrounds)

        # water
        # -----
        self.waterInput = QLineEdit(self)
        x = 330
        y = 730
        self.waterInput.move(x, y)
        self.waterInput.resize(txt_w,txt_h)
        # label
        self.setUnits(x,y,txt_h,"fl oz")
        # button
        self.measureWater = QPushButton("Add",self)
        self.measureWater.setGeometry(x+txt_w,y-2.5,50,txt_h+5)
        self.measureWater.clicked.connect(self.addWater)

        # Chemex
        # ------
        # Labels
        self.groundsLabel = QLabel(f"Grounds Added: {self.amt_grounds}.0 Tbsp",self)
        self.groundsLabel.setAlignment(Qt.AlignLeft)
        self.groundsLabel.setStyleSheet("background-color: white;")
        self.groundsLabel.setGeometry(695,500,150,15)

        self.waterLabel = QLabel(f"Water Added: {self.amt_water}.0 fl oz",self)
        self.waterLabel.setAlignment(Qt.AlignLeft)
        self.waterLabel.setStyleSheet("background-color: white;")
        self.waterLabel.setGeometry(710,500,150,15)
        # Button
        self.brewButton = QPushButton("Brew",self)
        self.brewButton.setGeometry(740,525,75,txt_h)

    def setUnits(self, x, y, height, label):
        """
        Sets a unit for the text entry
        """
        self.unit = QLabel(label, self)
        self.unit.setAlignment(Qt.AlignRight)
        self.unit.move(x+65,y+height/4)

    def addGrounds(self, checked):
        """
        Adds grounds to coffee
        """
        try:
            value = float(self.groundsInput.text())
            self.amt_grounds += value
        except ValueError:
            playAudio("doesnt_work",nancy=True)

    def addWater(self, checked):
        """
        Adds water to coffee
        """
        try:
            value = float(self.waterInput.text())
            self.amt_water += value
        except ValueError:
            playAudio("doesnt_work",nancy=True)

    def brewCoffee(self, checked):
        """
        Brews coffee based on grounds and water added
        """
        # checking to see if coffee has already been brewed
        if config.progress.made_coffee[0] == False:
            config.progress.made_coffee[0] = True # has been brewed
            if self.amt_grounds == 2 and self.amt_water == 8:
                config.progress.made_coffee[1] = True # has been brewed correctly
            else:
                config.progress.made_coffee[1] = False # has been brewed INcorrectly

            self.playAudio("done",nancy=True)
        else:
            self.playAudio("done_that",nancy=True)


    def updateMeasurements(self):
        # Update Text
        self.groundsLabel.setText(f"Grounds Added: {self.amt_grounds} Tbsp")
        self.waterLabel.setText(f"Water Added: {self.amt_water} fl oz")


