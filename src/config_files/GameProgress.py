import pandas as pd
import numpy as np

class Progress():
    def __init__(self):
        # Medals
        self.easter_egg_count = 0
        self.nugget_clicks = 0
        self.star_wars_count = 0
        self.pan_orchestra = 0

        # Easter Eggs
        self.ufo_clicked = False
        self.duct_clicked = False
        self.xwing_clicked = False
        self.ywing_clicked = False
        self.tie_clicked = False
        self.mixer_clicked = False

        # Story progress
        self.data = pd.read_csv("../data/progress.csv",index_col="name")
        self.data.replace(0,False)
        self.data.replace(1,True)

        # Game Flags
        self.message = False
        self.message_read = False
        self.service_status = "None"
        self.made_coffee = [False,False] # [isMade, isGood]

        # Story counters
        self.message_no = 1
        self.rooms_visited = 0

    # Coffee Methods
    # --------------
    def isCoffeeMade(self):
        """
        returns whether or not the coffee is made
        """
        return self.made_coffee[0]

    def isCoffeeGood(self):
        """
        returns whether or not the coffee is good
        """
        return self.made_coffee[1]

    def coffeeIsMade(self, flag):
        """
        Coffee is made set to flag
        """
        self.made_coffee[0] = flag

    def coffeeIsGood(self, flag):
        """
        Coffe is good set to flag
        """
        self.made_coffee[1] = flag