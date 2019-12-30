# Flappy bird type gravity and flight physics
# Using python 3 and turtle
# J Joubert 27 Dec 2019

import turtle

win = turtle.Screen()
win.title('Gravity simulation - "flappy ball"')
win.setup(850,600)
win.bgcolor('lightblue')
win.tracer(0)
win.listen()

class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__(shape='circle')
        self.color('red')
        self.up()
        self.goto(-410,200)
        self.dy = 0
        self.dx = 2


class Pen(turtle.Turtle):
    def __init__(self):
        super().__init__(shape='circle')
        self.hideturtle()
        self.up()
        self.color('red')
        self.goto(200,250)
        self.write('Press "Up" to fly', align='center', font=('Courier', 18, 'normal'))


class Ground(turtle.Turtle):
    def __init__(self):
        super().__init__(shape='square')
        self.shapesize(0.5, 40)
        self.up()
        self.goto(0, -275)
        self.color('green')

gravity = 0.09
remaining_energy = 0.8 # Amount of bounce at bottom

ball = Ball()
pen = Pen()
ground = Ground()

def move_up():
    ball.dy = 5
    

win.onkey(move_up, 'Up')

while True:
    win.update()

    ball.dy -= gravity   
    ball.goto(ball.xcor()+ball.dx, ball.ycor()+ball.dy)

    if ball.ycor() <= -260 and ball.dy<0:
        ball.dy *= -1
        ball.dy *= remaining_energy
        print(ball.dy)
        

    if ball.xcor()>400:
        ball.goto(-400,ball.ycor())
        

    
        

        


