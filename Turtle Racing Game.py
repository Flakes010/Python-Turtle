import turtle
import random


HEIGHT, WIDTH = 500, 500

COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']

def get_number_of_racers():
    racers = 0
    while True:
        racers = input('Enter the Turtle Number (2-10): ')
        if racers.isdigit():
            racers = int(racers)
        else:
            print('The Value you typed is not True... Try Again!')
            continue
    
        if 2 <= racers and 10 >= racers:
            return racers
        else:
            print("Entered Number is out of Range (2-10)... Try Again!")
            continue

def race(colors):
    turtles = createTurtles(colors)
    
    while True:
        for racer in turtles:
            distance = random.randrange(1,30)
            racer.forward(distance)

            x , y = racer.pos()
            if y >= HEIGHT // 2 - 30:
                return colors[turtles.index(racer)]


def createTurtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i + 1) * spacingx, -HEIGHT // 2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles

def showScreen():
    screen = turtle.Screen()
    screen.setup(HEIGHT, WIDTH)
    screen.title('Turtle Racing Game')

racers = get_number_of_racers()
showScreen()


random.shuffle(COLORS)
colors = COLORS[:racers]

#racer = turtle.Turtle()
winner = race(colors)
print("The Winner Color is {}".format(winner))

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()
t.goto(0, -HEIGHT // 2 + 20)
t.pendown()
t.color(winner)
t.write(winner + " won!", move=False, align='center', font=('arial', 15, 'normal'))

turtle.mainloop()
