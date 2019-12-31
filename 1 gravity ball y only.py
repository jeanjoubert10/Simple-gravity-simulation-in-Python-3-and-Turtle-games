# Simple gravity simulation in Python 3 and Turtle
# J Joubert 27 Dec 2019
# Written in osx and IDLE
# May need adjustment of speed in windows


import turtle
#import time # and time.sleep(0.017) windows??

win = turtle.Screen()
win.title('Gravity simulation - only in y axis')
win.setup(500,600)
win.tracer(0) # Stops animation until win.update() 


ball = turtle.Turtle()
ball.shape('circle')
ball.color('red')
ball.up() # Lift pen up
ball.goto(0,250)
ball.dy = 0

ground = turtle.Turtle()
ground.shape('square')
ground.shapesize(0.5, 20)
ground.up()
ground.goto(0, -275)
ground.color('green')

gravity = 0.09 # May need adjustment in windows
remaining_energy = 0.8 # Amount of bounce


while True:
    win.update()

    ball.dy -= gravity   
    ball.goto(ball.xcor(), ball.ycor()+ball.dy)

    if ball.ycor() <= -260 and ball.dy<0:
        ball.dy *= -1 # Change direction to up
        ball.dy *= remaining_energy # Keep 80% velocity
        print('dy = ',round(ball.dy,2)) # Round off to 2 decimal places
        
        if ball.dy <0.5: 
            break
        
    #time.sleep(0.017) # windows??

    
    
        

        


