import turtle

HEIGHT, WIDTH = 900, 900

screen = turtle.Screen()
screen.setup(HEIGHT, WIDTH)
screen.title('Spiral')

t = turtle.Turtle()
t.color('black')
t.pensize(2)
t.shape('arrow')
t.speed(5)

for i in range(50, 800, 20):
    t.forward(i)
    t.left(90)

turtle.mainloop()
