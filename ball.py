from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_speed = 10
        self.y_speed = -10
        self.goto(0, -270)
    def move(self):
        new_x = self.xcor() + self.x_speed
        new_y = self.ycor() + self.y_speed
        self.goto(new_x, new_y)
    def bounce(self):
        self.y_speed *= -1
    def hit(self):
        self.x_speed *= -1
    def increase_speed(self):
        self.x_speed *= 1.3
        self.y_speed *= 1.3



