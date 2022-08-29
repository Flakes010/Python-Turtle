import turtle

HEIGHT = 800
WIDTH = 800
PENSIZE = 3
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title('Turtle NotePad')
#turtle.screensize(canvheight=HEIGHT, canvwidth=WIDTH)
t = turtle.Turtle()
a = turtle.Turtle()
a.hideturtle()
t.speed(-1)
a.speed(-1)
t.pensize(PENSIZE)
t.shape('arrow')
FONTSIZE = 12
FONT = ('Arial', FONTSIZE, 'normal')


a.penup()
a.goto(-370,-370)
a.write("1 = Red  2 = Blue  3 = Purple  4 = Black  5 = Green  6 = Yellow  7 = Orange   8 = Eraser   Right Click = Clear", font=FONT) 
a.home()
a.pendown()



def RedChangeColor():
    t.color('red')
    t.pensize(3)

def BlueChangeColor():
    t.color('blue')
    t.pensize(3)

def PurpleChangeColor():
    t.color('purple')
    t.pensize(3)

def BlackChangeColor():
    t.color('black')
    t.pensize(3)

def GreenChangeColor():
    t.color('green')
    t.pensize(3)

def YellowChangeColor():
    t.color('yellow')
    t.pensize(3)

def OrangeChangeColor():
    t.color('orange')
    t.pensize(3)

def Eraser():
    t.color('white')
    t.pensize(50)

    

def dragging(x,y):
    t.ondrag(None)
    t.setheading(t.towards(x,y))
    t.goto(x,y)
    t.ondrag(dragging)

def mouseclickRight(x,y):
    t.clear()

def main():
    turtle.listen()

    t.ondrag(dragging)

    turtle.onscreenclick(mouseclickRight, 3)

    turtle.onkey(RedChangeColor, 1)
    turtle.onkey(BlueChangeColor, 2)
    turtle.onkey(PurpleChangeColor, 3)
    turtle.onkey(BlackChangeColor, 4)
    turtle.onkey(GreenChangeColor, 5)
    turtle.onkey(YellowChangeColor, 6)
    turtle.onkey(OrangeChangeColor, 7)
    turtle.onkey(Eraser, 8)

    turtle.mainloop()


main()
