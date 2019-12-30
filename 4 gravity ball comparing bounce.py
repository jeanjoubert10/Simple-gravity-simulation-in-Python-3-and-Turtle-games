# Comparing bounce in 3 different balls
# Gravity and bounce added as attributes so that it
# can be controlled individually
# J Joubert 27 Dec 2019

import turtle

win = turtle.Screen()
win.title('Gravity simulation - comparing 3 different loss of energy')
win.setup(850,600)
win.tracer(0)

class Ball(turtle.Turtle):
    def __init__(self, bounce, color, gravity):
        super().__init__(shape='circle')
        self.up()
        self.goto(-410,200)
        self.dy = 0
        self.dx = 1
        self.down()
        self.bounce = bounce
        self.color(color)
        self.gravity = gravity



ground = turtle.Turtle()
ground.shape('square')
ground.shapesize(0.5, 40)
ground.up()
ground.goto(0, -275)


ball = Ball(0.9, 'red', 0.09)
ball2 = Ball(0.8, 'blue', 0.09)
ball3 = Ball(0.7, 'green',0.09)

ball2.goto(ball2.xcor()+10, ball2.ycor())
ball3.goto(ball3.xcor()+20, ball3.ycor())

ball_list = [ball, ball2, ball3]

while True:
    win.update()

    for i in ball_list:
        i.dy -= i.gravity   
        i.goto(i.xcor()+i.dx, i.ycor()+i.dy)

        if i.ycor() <= -260 and i.dy<0:
            i.dy *= -1
            i.dy *= i.bounce
            
            if i.dy <0.5: # Balancing forces when at ground level
                i.dy = 0
                i.gravity  = 0
                i.bounce = 0

        if i.xcor()>400:
            break
    


        

    
        

        


