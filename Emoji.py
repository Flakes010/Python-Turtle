import turtle


HEIGHT, WIDTH = 800, 600

screen = turtle.Screen()
screen.setup(HEIGHT, WIDTH)
screen.title('Turtle Emoji')

t = turtle.Turtle()
t.hideturtle()
t.speed(5)
t.penup()
t.pendown()
t.pensize(2)
t.color('yellow')
t.begin_fill()
t.circle(100)
t.end_fill()

eye = turtle.Turtle()
eye.hideturtle()
eye.speed(5)
eye.color('black')
eye.pensize(5)
eye.penup()
eye.goto(45,130)
eye.dot(30)
eye.goto(-45,130)
eye.dot(30)

eye.goto(-65,65)
eye.pendown()
eye.setheading(-60)
eye.circle(80,120)

turtle.done()
