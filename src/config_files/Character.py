

class Nancy():

    def __init__(self):
        self.name = "Nancy"
        self.item = None

    def setItem(self, item):
        self.item = item

    def hasItem(self):
        if self.item == None:
            return False
        else:
            return True

class Ingman():

    def __init__(self):
        self.name = "Ingman"

        