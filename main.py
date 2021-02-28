import tkinter as tk
from random import randint

class ColorHEX:
    red: str = '#FF0000'
    green: str = '#00FF00'
    blue: str = '#0000FF'

class MainWindow(tk.Tk):

    def __init__(self):
        super().__init__()
        self._initUI()
        self.mainloop()

    def _initUI(self):
        self.geometry('600x480')
        self.title('Система управления')
        self.field = GameField()
        self.target = Oval(self.field, (40, 40), ColorHEX.red)



class GameField(tk.Canvas):

    def __init__(self, width=400, height=400):
        super().__init__(width=width, height=height)
        self.width = 400
        self.height = 400
        self._initUI()
    
    def _initUI(self):
        self.place(x=30, y=30)

    
class Oval:

    def __init__(self, field: GameField, size: tuple, color: ColorHEX):
        self.field = field
        self.size = size
        self.width = size[0]
        self.height = size[1]
        self.x = randint(0, field.width - self.width)
        self.y = randint(0,field.height - self.height) 
        self.color = color
    
    def draw(self):
        self.field.create_oval(self.x, self.y, self.x + self.width, self.y + self.height, fill=self.color)






MainWindow()