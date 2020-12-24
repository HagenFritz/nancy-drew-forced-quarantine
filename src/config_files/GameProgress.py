import pandas as pd
import numpy as np

from Screen import FatalError

class Progress():
    def __init__(self):
        # Medals
        self.easter_egg_count = 0 # keeps track of easter eggs found
        self.nugget_clicks = 0 # keeps track of the number of times the person clicks the nugget
        self.star_wars_count = 0 # keeps track of the number of star wars items clicked
        self.pan_orchestra = 0 # keeps track of the number of pans clicked
        self.lights_switched = 0 # keeps track of the number of times the user turns the lights off

        # Easter Eggs
        self.ufo_clicked = False
        self.duct_clicked = False # Could be name associated with Eugene Tombs
        self.xwing_clicked = False
        self.ywing_clicked = False
        self.tie_clicked = False
        self.mixer_clicked = False

        # Story progress
        self.data = pd.read_csv("../data/progress.csv",index_col="name")
        self.data.replace(0,False)
        self.data.replace(1,True)

        # Game Flags
        self.message = True
        self.message_read = True
        self.service_status = "None"
        self.made_coffee = [False,False] # [isMade, isGood]

        # Fatal Error 
        self.fe  = None
        self.jumped_off_balcony = False

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

    # Fatal Error
    # -----------
    def fatalError(self):
        """
        Tatal Error message when the user messes up in the game. Messages to send are based on progress and various flags.
        """
        if self.fe is None:
            self.fe = FatalError()
            self.fe.show()
        else:
            self.fe.close()
            self.fe = None

