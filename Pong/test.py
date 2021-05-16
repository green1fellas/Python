import turtle

# SETUP

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)

# PADDLE A

paddle_a = turtle.Turtle()
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)

paddle_a.color("white")
paddle_a.penup()
paddle_a.speed(0)
paddle_a.goto(-350, 0)

#Functions

def paddle_a_up():
  y = paddle_a.ycor()
  y = y + 20
  paddle_a.sety(y)

wn.listen()
wn.onkeypress(paddle_a_up, "w")

while(True):
    wn.update()