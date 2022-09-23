import turtle
import datetime

screen = turtle.Screen()
screen.setup(600,600)
screen.title('Clock')
#screen.bgcolor('black')
screen.bgpic('8i65rRgLT.png')

hour = turtle.Turtle()
hour.hideturtle()
hour.pensize(7)
hour.speed(0)
hour.color('black')
hour.shape('arrow')
hour.turtlesize(1.5,1.5)

minute = turtle.Turtle()
minute.hideturtle()
minute.pensize(7)
minute.speed(0)
minute.color('black')
minute.shape('arrow')
minute.turtlesize(1.5,1.5)

second = turtle.Turtle()
second.hideturtle()
second.pensize(3)
second.speed(0)
second.color('red')
second.shape('arrow')
second.turtlesize(0.5,0.5)

x, y, z = -1, -1, -1

while True:
    today = datetime.datetime.today()

    if today.hour != x:
        hour.home()
        hour.clear()
        hour.setheading(90)
        hour.right((today.hour % 12)*30 + today.minute//2)
        hour.forward(100)
    
    if today.minute != y:
        minute.home()
        minute.clear()
        minute.setheading(90)
        minute.right(today.minute*6)
        minute.forward(150)
    
    if today.second != z:
        second.home()
        second.clear()
        second.setheading(90)
        second.right(today.second*6)
        second.forward(180)

    x = today.hour
    y = today.minute
    z = today.second

turtle.mainloop()
