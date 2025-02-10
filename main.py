from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
game_is_on = True
screen.tracer(0)
paddle_r = Paddle((370, 0))
paddle_l = Paddle((-370, 0))
ball = Ball()
scoreboard = Scoreboard()
scoreboard.update_scoreboard()
screen.update()
screen.listen()
screen.onkey(paddle_l.move_up, "w")
screen.onkey(paddle_l.move_down, "s")
screen.onkey(paddle_r.move_up, 'Up')
screen.onkey(paddle_r.move_down , 'Down')
while game_is_on:
    screen.update()
    ball.move()
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce()
    
    if ball.xcor() >= 350 or ball.xcor() <= -350:
        if ball.distance(paddle_l) < 50 or ball.distance(paddle_r) < 50:
            ball.hit()
            scoreboard.update_scoreboard()
            if scoreboard.score % 4 == 0:
                ball.increase_speed()
    
    if ball.xcor() > 390 or ball.xcor() < -390:
        game_is_on = False
        scoreboard.game_over()
    time.sleep(0.1)
screen.exitonclick()