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
        self.geometry('800x460')
        self.title('Система управления')
        self.field = GameField()
        self.target = Oval(self.field, (40, 40), ColorHEX.red)
        self.player = Oval(self.field, (20, 20), ColorHEX.blue)
        self.game_control = GameControl(self.player)
        self.target.draw()
        self.player.draw()



class GameField(tk.Canvas):

    def __init__(self, width=400, height=400):
        super().__init__(width=width, height=height, bg=ColorHEX.green)
        self.width = 400
        self.height = 400
        self.ceil = 20
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
    
    def move_up(self):
        self.y -= self.field.ceil

    def move_down(self):
        self.y += self.field.ceil
    
    def move_left(self):
        self.x -= self.field.ceil

    def move_right(self):
        self.x += self.field.ceil


class GameControl(tk.Frame):
    """Джостик, для управления игроком

    Arguments:
        tk {Frame} -- Рамка джостика, определяет положение джостика и его размер
    """

    def __init__(self, player: Oval):
        super().__init__()
        self.player = player
        self.width = 20
        self.height = 20
        self.btn_up = tk.Button(self, command=player.move_up)
        self.btn_down = tk.Button(self, command=player.move_down)
        self.btn_right = tk.Button(self, command=player.move_right)
        self.btn_left = tk.Button(self, command=player.move_left)
        self._initUI()
    
    def _initUI(self):
        self.place(x=460, y=400)
        self.btn_up.grid(row=0, column=1)
        self.btn_left.grid(row=1, column=0)
        self.btn_right.grid(row=1, column=2)
        self.btn_down.grid(row=2, column=1)







MainWindow()