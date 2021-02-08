import tkinter as tk


class MainWindow(tk.Tk):
    """Main window app"""

    def __init__(self, screenName=None, baseName=None, useTk=1, sync=0, use=None):
        super().__init__(screenName=screenName, baseName=baseName, useTk=useTk, sync=sync, use=use)
        self.init_window()
        self.initUI()
        self.mainloop()
    
    def init_window(self):
        self.title('Control System')
        self.geometry('600x420')
    
    def initUI(self):
        self.field = GameField(self, width=400, height=400, bg='gray')
        self.jostic = GameControl(self)


class GameField(tk.Canvas):
    def __init__(self, master=None, **kw):
        super().__init__(master=master, **kw)
        self.initUI()
    
    def initUI(self):
        self.place(x=10, y=10)


class GameControl(tk.Frame):


    def __init__(self, master, **kw):
        super().__init__(master=master, **kw)
        self.up = tk.Button(self, text='UP',  bg='silver')
        self.down = tk.Button(self, text='DOWN',  bg='silver')
        self.left = tk.Button(self, text='LEFT',  bg='silver')
        self.right = tk.Button(self, text='RIGHT',  bg='silver')

        self.initUI()

    
    def initUI(self):
        [self.grid_columnconfigure(i, minsize=50) for i in range(3)]
        [self.grid_rowconfigure(i, minsize=50) for i in range(3)]
        self.place(x=430, y=260)
        self.up.grid(row=0, column=1, sticky='wens')
        self.down.grid(row=2, column=1, sticky='wens')
        self.left.grid(row=1, column=0, sticky='wens')
        self.right.grid(row=1, column=2, sticky='wens')

