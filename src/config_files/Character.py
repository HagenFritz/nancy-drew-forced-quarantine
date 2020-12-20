import config

class Nancy():

    def __init__(self,inventory_from_savefile=False):
        self.name = "Nancy Drew"
        self.item = None
        if inventory_from_savefile:
            self.inventory = config.load("../data/save_files/","inventory","_test")
        else:
            self.inventory = ["bag","filters","grounds","chemex","mug"]

    def setItem(self, item):
        self.item = item

    def hasItem(self):
        if self.item == None:
            return False
        else:
            return True

    def getInventory(self):
        """
        Returns sorted inventory
        """
        self.inventory.sort()
        return self.inventory

class Ingman():

    def __init__(self):
        self.name = "Waltz Ingman"

        