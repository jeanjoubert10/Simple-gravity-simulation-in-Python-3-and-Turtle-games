# Playing with simple gravity simulation in Python 3 and Turtle
# J Joubert 27 Dec 2019
# gravity/bounce/lateral movement
# wind acting in the same way as gravity but to the left
# OSX and IDLE - may need adjustment in windows

import turtle
import random
#import time # and time.sleep(0.017) windows??

win = turtle.Screen()
win.title('Gravity simulation - some wind from right')
win.setup(850,600)
win.tracer(0)


class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__(shape='circle')
        self.color('red')
        self.up()
        self.goto(-410,280)
        self.dy = 0
        self.dx = 1 # windows ??0.01
        self.down()


# Only to visualize the wind but not needed:
class Wind(turtle.Turtle):
    def __init__(self):
        super().__init__(shape='circle')
        self.shapesize(0.1,0.1) #resize 10%x and 10%y (2x2 pixels)
        self.up()
        self.color('blue')
        self.goto(random.randint(-420,420), random.randint(-280,280))
        self.dx = -0.5 # windows ??0.005

    def move(self):
        self.goto(self.xcor()+self.dx, self.ycor())
        if self.xcor()<=-430:
            self.goto(420, self.ycor())


class Ground(turtle.Turtle):
    def __init__(self):
        super().__init__(shape='square')
        self.shapesize(0.5, 40)
        self.up()
        self.goto(0, -275)

gravity = 0.09 # May need adjustment in windows
remaining_energy = 0.9
windspeed = 0.001 # wind from the right
wind_list = []

ball = Ball()
ground = Ground()


for i in range(100):
    wind = Wind()
    wind_list.append(wind)

while True:
    win.update()
    #time.sleep(0.017) # windows??

    for i in wind_list:
        i.move()

    ball.dy -= gravity
    if ball.dx >= -0.5:
        ball.dx -= windspeed
    
    ball.goto(ball.xcor()+ball.dx, ball.ycor()+ball.dy)

    if ball.ycor() <= -260 and ball.dy<0:
        ball.dy *= -1
        ball.dy *= remaining_energy
        #print('ball.dy = ',round(ball.dy,2),'ball.dx = ', round(ball.dx,2))
        if ball.dy <0.5:
            ball.dy = 0
            gravity  = 0
            remaining_energy = 0

    if ball.xcor()>400:
        break
        

    
        

        


