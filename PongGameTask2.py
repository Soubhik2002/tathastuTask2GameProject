

# Pong game code starts from here:-

import turtle
import os

wn = turtle.Screen()
wn.title("Pong Game By @SoubhikAcharya")                # Title of the game.
wn.bgcolor("Black")                                     # Here we are giving background color to the game screen.
wn.setup(width=800, height=600)                         # setting up the height and width of the game screen.
wn.tracer(0)


# Score

score_a = 0    # Player A Score will be displayed when striking.
score_b = 0    # Player B Score will be displayed when striking.

# For the Paddle A

paddle_a = turtle.Turtle()
paddle_a.speed(0) # paddle speed.
paddle_a.shape("square") # Here we are giving the shape, how it will look like either square, rectangle, etc. as per choice.
paddle_a.color("red")  # Here we are defining the color of paddle A.
paddle_a.shapesize(stretch_wid=5,stretch_len=1)  # size definition of the paddle.
paddle_a.penup()    # for lifting
paddle_a.goto(-350, 0)   # Here we are taking -350 because we are shifting the paddle to left side of the game screen.

# For the Paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0) # paddle speed.
paddle_b.shape("square") # Here we are giving the shape, how it will look like either square, rectangle, etc. as per choice.
paddle_b.color("red")  # Here we are defining the color of paddle B.
paddle_b.shapesize(stretch_wid=5,stretch_len=1) # size definition of the paddle.
paddle_b.penup()     # for lifting
paddle_b.goto(350, 0)   # Here we are taking -350 because we are shifting the paddle to left side of the game screen.


# For the Pong Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")    # defining the shape of the ball how it will appear square, rectangle or circle shape.
ball.color("Yellow")     # defining the color of the ball.
ball.penup()            # for lifting.
ball.goto(0, 0)
ball.dx = 0.1             # axis definition
ball.dy = 0.1             # axis definition

# Code for Pen

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Writing Functions for moving the Paddle Up and Down.

def paddle_a_up():
    y = paddle_a.ycor()
    y += 30
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 30
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 30
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 30
    paddle_b.sety(y)

# Keyboard bindings


wn.listen()

# for paddle A stating the Keys which key by pressing will push the paddle A to up and which key will move the paddle A to down.

wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")

# for paddle B stating the Keys which key by pressing will push the paddle B to up and which key will move B to down.

wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")



# <-------- Main Game Loop is starting From Here -------->

while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking

    # Top and bottom


    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")
    
    
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    # Left and right


    if ball.xcor() > 350:
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -350:
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    # Code for paddle and ball collisions :-


    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1 
        os.system("afplay bounce.wav&")
    
    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
        os.system("afplay bounce.wav&")
    
