class Dummys:
    def __init__(self,dummys):
        self.dummys = dummys
    def pop(self):
        self.dummys.pop()

class Floor:
    def __init__(self, flr):
        self.floor = []
        for card in flr:
            self.floor.append(card.split(' '))
    def append(self,card):
        self.floor.append(card.split(' '))
    def pop(self,index):
        self.floor.pop(index)