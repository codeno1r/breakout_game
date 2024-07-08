from time import sleep
from turtle import Screen
from paddle import Paddle
from ball import Ball
from bricks import Bricks
from scoreboard import Scoreboard
from ui import UI

root = Screen()
root.setup(width=600, height=800)
root.bgcolor('black')
root.title('codenoir: Breakout Game')
root.tracer(0)

paddle = Paddle()
ball = Ball()
bricks = Bricks()
scoreboard = Scoreboard()
ui = UI()
ui.header()

top_wall = 395
bottom_wall = -390
left_wall = -295
right_wall = 290


def pause_game():
    if ui.game_paused:
        ui.game_paused = False
    else:
        ui.game_paused = True


root.listen()
root.onkeypress(fun=paddle.move_left, key='a')
root.onkeypress(fun=paddle.move_right, key='d')
root.onkey(fun=pause_game, key='space')


def check_wall_collision():
    if ball.ycor() >= top_wall:
        ball.bounce(bounce_x=False, bounce_y=True)
    elif ball.xcor() <= left_wall:
        ball.bounce(bounce_x=True, bounce_y=False)
    elif ball.xcor() >= right_wall:
        ball.bounce(bounce_x=True, bounce_y=False)
    elif ball.ycor() <= bottom_wall:
        ball.reset()
        # scoreboard.update_lives()
        if scoreboard.lives == 0:
            scoreboard.reset_score()
            ui.playing_game = False
            ui.game_over(win=False)
            return
        ui.change_color()
        return


def check_paddle_collision():
    if ball.distance(paddle) < 110 and ball.ycor() < -350:
        if paddle.left_wall < paddle.right_wall <= ball.xcor():
            print(f'leftWall: {paddle.left_wall} | rightWall: {paddle.right_wall} | ballXCor: {ball.xcor()}')
            ball.bounce(bounce_x=True, bounce_y=False)
            return
        elif ball.xcor() <= paddle.left_wall < paddle.right_wall:
            print(f'ballXCor: {ball.xcor()} | leftWall: {paddle.left_wall} | rightWall: {paddle.right_wall}')
            ball.bounce(bounce_x=True, bounce_y=False)
            return
        else:
            print(f'leftWall: {paddle.left_wall} | ballXCor: {ball.xcor()} | rightWall: {paddle.right_wall}')
            ball.bounce(bounce_x=False, bounce_y=True)
            return


def check_brick_collision():
    for brick in bricks.all_bricks:
        if ball.distance(brick) < 40:
            if ball.xcor() < brick.left_wall:
                ball.bounce(bounce_x=True, bounce_y=False)
                bricks.all_bricks.pop(bricks.all_bricks.index(brick))
                brick.hideturtle()
                scoreboard.update_score(score=10)
                return
            elif ball.xcor() > brick.right_wall:
                ball.bounce(bounce_x=True, bounce_y=False)
                bricks.all_bricks.pop(bricks.all_bricks.index(brick))
                brick.hideturtle()
                scoreboard.update_score(score=7)
                return
            elif ball.ycor() > brick.top_wall:
                ball.bounce(bounce_x=False, bounce_y=True)
                bricks.all_bricks.pop(bricks.all_bricks.index(brick))
                brick.hideturtle()
                scoreboard.update_score(score=7)
                return
            elif ball.ycor() > brick.bottom_wall:
                ball.bounce(bounce_x=False, bounce_y=True)
                bricks.all_bricks.pop(bricks.all_bricks.index(brick))
                brick.hideturtle()
                scoreboard.update_score(score=5)
                return


while ui.playing_game:
    if not ui.game_paused:
        root.update()
        sleep(0.001)
        ball.move()
        check_wall_collision()
        check_paddle_collision()
        check_brick_collision()

        if len(bricks.all_bricks) == 0:
            ui.game_over(win=True)
            break

    else:
        root.update()
        sleep(0.001)
        ui.paused_status()

root.mainloop()
