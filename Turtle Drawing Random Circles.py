import turtle
import random

t = turtle.Turtle()
colors = ["red", "blue", "purple", "black", "yellow", "green", "orange"]
t.color("red")
t.pensize(5)
t.speed(0)


for i in range(5):
    randColor = random.randrange(0,len(colors))
    t.color(colors[randColor], colors[random.randrange(0,len(colors))])
    rand1 = random.randint(-300,300)
    rand2 = random.randint(-300,300)
    t.penup()
    t.setpos(rand1,rand2)
    t.pendown()
    t.begin_fill()
    t.circle(random.randrange(20,80))
    t.end_fill()

turtle.done()
