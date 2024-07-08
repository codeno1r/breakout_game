from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=10)
        self.color('white')
        self.goto(x=0, y=-370)
        self.top_wall = self.ycor() + 10
        self.left_wall = self.xcor() - 101
        self.right_wall = self.xcor() + 108

    def move_left(self):
        new_x = self.xcor() - 20
        if self.xcor() >= -190:
            self.setx(new_x)
        self.left_wall = new_x - 101
        self.right_wall = new_x + 108

    def move_right(self):
        new_x = self.xcor() + 20
        if self.xcor() <= 190:
            self.setx(new_x)
        self.left_wall = new_x - 101
        self.right_wall = new_x + 108
