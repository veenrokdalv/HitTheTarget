from random import randrange


class Target:

    def __init__(self):
        self.x = randrange(0, 400)
        self.y = randrange(0, 400)
        self.color = 'red'
        self.radius = 20




class Player:
    
    def __init__(self):
        self.x = randrange(0, 400)
        self.y = randrange(0, 400)
        self.color = 'red'
        self.radius = 10


class GameManager:
     
    def __init__(self):
        self.player = Player()
        self.target = Target()