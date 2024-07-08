from turtle import Turtle
from random import choice

COLOR_LIST = ['light blue', 'royal blue',
              'light steel blue', 'steel blue',
              'light cyan', 'light sky blue',
              'violet', 'salmon', 'tomato',
              'sandy brown', 'purple', 'deep pink',
              'medium sea green', 'khaki']


class Brick(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color(color)
        self.shapesize(stretch_wid=1.5, stretch_len=4)
        self.goto(position)
        self.top_wall = self.ycor() + 15
        self.bottom_wall = self.ycor() - 15
        self.left_wall = self.xcor() - 40
        self.right_wall = self.xcor() + 40


class Bricks:
    def __init__(self):
        self.all_bricks = []
        self.starting_y = 310
        self.starting_x = -256
        self.place_bricks()

    def place_bricks(self):
        for _ in range(0, 5):
            column = self.starting_x
            color = choice(COLOR_LIST)
            for _ in range(0, 7):
                position = (column, self.starting_y)
                self.add_brick(position, color)
                column += 84
            self.starting_y -= 34

    def add_brick(self, position, color):
        brick = Brick(position, color)
        self.all_bricks.append(brick)
