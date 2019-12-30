# Simple program to show gravity and bounce with side movement
# J Joubert 27 Dec 2019


import turtle

win = turtle.Screen()
win.title('Gravity simulation - with side movement')
win.setup(850,600)
win.tracer(0) # Stops animation until win.update()


ball = turtle.Turtle()
ball.shape('circle')
ball.color('red')
ball.up() # Lift pen up
ball.goto(-410,200)
ball.dy = 0
ball.dx = 1 # will move to the right 1 pixel/loop
ball.down() # put pen down for drawing

ground = turtle.Turtle()
ground.shape('square')
ground.shapesize(0.5, 40) # turtle is looking to Right, 0.5x and 40y stretch
ground.up()
ground.goto(0, -275)
ground.color('green')

gravity = 0.09
remaining_energy = 0.8 # increase for more bounce, decrease for less 


while True:
    win.update()

    ball.dy -= gravity   
    ball.goto(ball.xcor()+ball.dx, ball.ycor()+ball.dy)

    if ball.ycor() <= -260 and ball.dy<0:
        ball.dy *= -1
        ball.dy *= remaining_energy
        print('ball.dy = ',round(ball.dy,2)) # Round off to 2 decimal places
        if ball.dy <0.5:
            ball.dy = 0
            gravity  = 0
            remaining_energy = 0

    if ball.xcor()>400:
        break
        

    
        

        


