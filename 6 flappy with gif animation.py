# Flappy bird type animation/flight
# Playing with simple gravity in Python 3 and Turtle
# J Joubert 27 Dec 2019

import turtle

win = turtle.Screen()
win.title('Gravity simulation - bouncing bird and simple gif animation')
win.setup(850,600)

win.bgpic('background.gif')
win.tracer(0)
win.listen()

win.register_shape('b1.gif')
win.register_shape('b2.gif')


class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__(shape='circle')
        self.color('red')
        self.up()
        self.s = 'b1.gif' # used for - if statement to assess shape
        self.shape(self.s)
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


gravity = 0.09
remaining_energy = 0.8 # amount of bounce when hitting ground

ball = Ball()
pen = Pen()


def move_up():
    ball.dy = 5 # upward motion
    

win.onkey(move_up, 'Up')

counter = 0 # used to time the gif animation


while True:
    win.update()

    ball.dy -= gravity   
    ball.goto(ball.xcor()+ball.dx, ball.ycor()+ball.dy)

    # Bounce
    if ball.ycor() <= -260 and ball.dy<0:
        ball.dy *= -1
        ball.dy *= remaining_energy
        #print(ball.dy)


    # Back to left side of screen
    if ball.xcor()>400:
        ball.goto(-400,ball.ycor())


    # Simple gif animation:
    if ball.s == 'b1.gif' and counter%5 == 0: # change only every 5th time in the loop (not too quickly)
        ball.s = 'b2.gif'
        ball.shape(ball.s)
    elif ball.s == 'b2.gif' and counter%5 == 0:
        ball.s = 'b1.gif'
        ball.shape(ball.s)
        
    counter += 1
        

    
        

        


