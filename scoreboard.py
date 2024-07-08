from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.score = 0
        self.lives = 3
        try:
            with open('highscore.txt', 'r') as hs:
                self.highscore = int(hs.read())
        except FileNotFoundError:
            with open('highscore.txt', 'w') as hs:
                hs.write(str(self.score))
            with open('highscore.txt', 'r') as hs:
                self.highscore = int(hs.read())
                self.update_scoreboard()
        else:
            self.update_scoreboard()

    def reset_score(self):
        self.score = 0
        self.update_scoreboard()

    def update_score(self, score):
        self.score += score
        if self.score > self.highscore:
            self.update_highest_score()
        self.update_scoreboard()

    def update_highest_score(self):
        with open('highscore.txt', 'w') as hs:
            hs.write(str(self.score))
        with open('highscore.txt', 'r') as hs:
            self.highscore = int(hs.read())

    def update_lives(self):
        self.lives -= 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(x=-290, y=370)
        self.write(f'Score: {self.score}', font=('Courier', 14, 'bold'))
        self.goto(x=-290, y=350)
        self.write(f'Highest Score: {self.highscore}', font=('Courier', 14, 'bold'))
        self.goto(x=-290, y=330)
        self.write(f'Lives: {self.lives}', font=('Courier', 14, 'bold'))