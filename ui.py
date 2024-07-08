from turtle import Turtle
from random import choice
from time import sleep

FONT = ("Courier", 32, "normal")
FONT2 = ("Courier", 32, "normal")
ALIGNMENT = 'center'
COLOR = "white"
COLOR_LIST = ['light blue', 'royal blue',
              'light steel blue', 'steel blue',
              'light cyan', 'light sky blue',
              'violet', 'salmon', 'tomato',
              'sandy brown', 'purple', 'deep pink',
              'medium sea green', 'khaki']


class UI(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color(choice(COLOR_LIST))
        self.header()
        self.playing_game = True
        self.game_paused = False

    def header(self):
        self.clear()
        self.goto(x=55, y=350)
        self.write('Breakout', align=ALIGNMENT, font=FONT)
        self.goto(x=210, y=360)
        self.write('by <codenoir>', align=ALIGNMENT, font=('Calibri', 9, 'italic'))
        self.goto(x=100, y=332)
        self.write('Press Space to PAUSE or RESUME the Game',
                   align=ALIGNMENT, font=('Calibri', 11, 'italic'))

    def change_color(self):
        self.clear()
        self.color(choice(COLOR_LIST))
        self.header()

    def paused_status(self):
        self.clear()
        self.change_color()
        sleep(0.5)

    def game_over(self, win):
        if win:
            self.goto(x=0, y=0)
            self.write('You Cleared the Game', align='center', font=FONT)
        else:
            self.goto(x=0, y=0)
            self.write("Game is Over", align='center', font=FONT)
