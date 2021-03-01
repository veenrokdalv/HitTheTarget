import tkinter as tk
from random import randrange

class ColorHEX:
    red: str = '#FF0000'
    green: str = '#00FF00'
    blue: str = '#0000FF'

class MainWindow(tk.Tk):

    def __init__(self):
        super().__init__()
        self._initUI()
        self._init_game()
        self.mainloop()

    def _initUI(self):
        self.geometry('800x460')
        self.title('Система управления')
    
    def _init_game(self):
        self.field = GameField()
        self.target = Oval(self.field, (40, 40), ColorHEX.red)
        self.player = Oval(self.field, (20, 20), ColorHEX.blue)
        self.game_manager = GameMode()
        self.game_control = GameControl(self.player)



class GameField(tk.Canvas):

    def __init__(self, width=500, height=440):
        super().__init__(width=width, height=height, bg=ColorHEX.green)
        self.width = width
        self.height = height
        self.ceil = 20
        self._initUI()
    
    def _initUI(self):
        self.place(x=10, y=10)

    
class Oval:

    def __init__(self, field: GameField, size: tuple, color: ColorHEX):
        self.field = field
        self.size = size
        self.width = size[0]
        self.height = size[1]
        self.color = color
    
    def draw(self):
        self.field.create_oval(self.x, self.y, self.x + self.width, self.y + self.height, fill=self.color)
    
    def random_position(self):
        self.x = randrange(0, self.field.width - self.width, self.field.ceil)
        self.y = randrange(0, self.field.height - self.height, self.field.ceil)
    
    def move_up(self):
        if self.y > 0:
            self.y -= self.field.ceil

    def move_down(self):
        if self.y < self.field.height - self.height:
            self.y += self.field.ceil
    
    def move_left(self):
        if self.x > 0:
            self.x -= self.field.ceil

    def move_right(self):
        if self.x < self.field.width - self.width:
            self.x += self.field.ceil


class GameControl(tk.Frame):
    """Джостик, для управления игроком

    Arguments:
        tk {Frame} -- Рамка джостика, определяет положение джостика и его размер
    """

    def __init__(self, player: Oval):
        super().__init__()
        self.player = player
        self.width = 50
        self.height = 50
        self.btn_up = tk.Button(self, text='UP', command=player.move_up)
        self.btn_down = tk.Button(self, text='DOWN', command=player.move_down)
        self.btn_right = tk.Button(self, text='RIGHT', command=player.move_right)
        self.btn_left = tk.Button(self, text='LEFT', command=player.move_left)
        self._initUI()
    
    def _initUI(self):
        self.place(x=520, y=300)
        [self.grid_columnconfigure(i, minsize=self.width) for i in range(3)]
        [self.grid_rowconfigure(i, minsize=self.height) for i in range(3)]
        self.btn_up.grid(row=0, column=1, sticky='wens')
        self.btn_left.grid(row=1, column=0, sticky='wens')
        self.btn_right.grid(row=1, column=2, sticky='wens')
        self.btn_down.grid(row=2, column=1, sticky='wens')

class GameMode(tk.Frame):

    def __init__(self):
        super().__init__()
        self.mode = tk.IntVar()
        self.rb_mode1 = tk.Radiobutton(self, text='Режим 1', value=1, variable=self.mode)
        self.rb_mode2 = tk.Radiobutton(self, text='Режим 2', value=2, variable=self.mode)
        self.rb_mode3 = tk.Radiobutton(self, text='Режим 3', value=3, variable=self.mode)
        self._initUI()
    
    def _initUI(self):
        self.place(x=680, y=370)
        self.rb_mode1.grid(column=0, row=0)
        self.rb_mode2.grid(column=0, row=1)
        self.rb_mode3.grid(column=0, row=2)

MainWindow()