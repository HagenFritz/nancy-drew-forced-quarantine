import config

class Nancy():

    def __init__(self):
        self.name = "Nancy Drew"
        self.item = None
        self.inventory = []

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

        