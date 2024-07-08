from turtle import Turtle
from random import choice


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('white')
        self.start_one = 1
        self.start_two = self.start_one * -1
        self.step_x = choice([self.start_one, self.start_two])
        self.step_y = choice([self.start_one, self.start_two])

    def move(self):
        new_x = self.xcor() + self.step_x
        new_y = self.ycor() + self.step_y
        self.goto(new_x, new_y)

    def bounce(self, bounce_x, bounce_y):
        if bounce_x:
            self.step_x *= -1
        if bounce_y:
            self.step_y *= -1

    def reset(self):
        self.hideturtle()
        self.goto(0, 0)
        self.start_one = choice([1, -1])
        self.start_two = self.start_one * -1
        self.step_x = choice([self.start_one, self.start_two])
        self.step_y = choice([self.start_one, self.start_two])
        self.move()
        self.showturtle()
