import turtle
import random

# SETUP
bx = 0

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) # Speeds things up

# PADDLE A

paddle_a = turtle.Turtle()
paddle_a.speed(0) #animation speed
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# PADDLE B

paddle_b = turtle.Turtle()
paddle_b.speed(0) #animation speed
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# BALL

ball_a = turtle.Turtle()
ball_a.speed(0) #animation speed
ball_a.shape("square")
ball_a.color("white")
ball_a.penup()
ball_a.goto(0, 0)

# Function

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

def xCollisionChecks():

    # Paddle A
    paddle_aX = paddle_a.xcor()
    paddle_aYT = paddle_a.ycor() + 50
    paddle_aYB = paddle_a.ycor() - 50

    if(ball_a.xcor() < paddle_aX and 
    ball_a.ycor() < paddle_aYT and 
    ball_a.ycor() > paddle_aYB):
        return -1

    # Paddle B
    paddle_bX = paddle_b.xcor()
    paddle_bYT = paddle_b.ycor() + 50
    paddle_bYB = paddle_b.ycor() - 50

    if(ball_a.xcor() > paddle_bX and 
    ball_a.ycor() < paddle_bYT and 
    ball_a.ycor() > paddle_bYB):
        return -1

    return 1

def yCollisionChecks():
    global potato
    if(ball_a.ycor() < -300 or ball_a.ycor() > 300):
        return -1
    return 1
    
direction = 'up'


# Keyboard binding

wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.listen()

# GAME LOOP

turtle.color("orange")
turtle.write("score", font=("Arial", 16, "normal"))


speedX = .4
speedY = .4

while(True):
    speedX = speedX * xCollisionChecks()
    speedY = speedY * yCollisionChecks()
    bx = ball_a.xcor()
    by = ball_a.ycor()
    bx = bx - speedX
    by = by - speedY

    ball_a.setx(bx)
    ball_a.sety(by)

    wn.update()

