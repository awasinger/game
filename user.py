import items

class User():

    def __init__(self):
        self.pos = (0, 0, 0)
    
    def move(self, dir):
        next = items.checkEmpty(dir)
        if next:
            self.pos = next


user = User()
