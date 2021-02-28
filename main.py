import tkinter as tk
from random import randint

class MainWindow(tk.Tk):

    def __init__(self):
        super().__init__()
        self._initUI()
        self.mainloop()

    def _initUI(self):
        self.geometry('600x480')
        self.title('Система управления')
        self.field = GameField()
        self.target = Target(self.field)
        self.target.draw()


class GameField(tk.Canvas):

    def __init__(self, width=400, height=400):
        super().__init__(width=width, height=height)
        self.width = 400
        self.height = 400
        self._initUI()
    
    def _initUI(self):
        self.place(x=0, y=0)
    
class Target:

    def __init__(self, field: GameField):
        self.field = field
        self.x = randint(0, field.width)
        self.y = randint(0,field.height) 
        self.width = 20
        self.height = 20
        self.color = '#FF0000'
    
    def draw(self):
        self.field.create_oval(self.x, self.y, self.x + self.width, self.y + self.height, fill=self.color)






MainWindow()