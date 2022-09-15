import turtle
import random


t = turtle.Turtle()
t.speed(0)
t.width(5)

colors = ["red", "blue", "green", "yellow", "black"]

def up():
    t.setheading(90)
    t.forward(100)

def down():
    t.setheading(270)
    t.forward(100)

def right():
    t.setheading(0)
    t.forward(100)

def left():
    t.setheading(180)
    t.forward(100)

def mouseclickleft(x,y):
    t.color(random.choice(colors))

def mouseclickright(x,y):
    t.stamp()

turtle.listen()

turtle.onscreenclick(mouseclickleft, 1)
turtle.onscreenclick(mouseclickright, 3)

turtle.onkey(up, "Up")
turtle.onkey(down, "Down")
turtle.onkey(right, "Right")
turtle.onkey(left, "Left")

turtle.mainloop()
