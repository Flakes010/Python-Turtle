import turtle
import time

HEIGHT, WIDTH = 600, 800
run = True

scoring = turtle.Turtle()
scoring.hideturtle()
scoring.penup()
scoring.sety(250)
scoring.color('white')

def  showScreen():
    screen = turtle.Screen()
    screen.bgcolor(0,0,0)
    screen.setup(WIDTH,HEIGHT)
    screen.title('Pong Game')
    screen.tracer(1)

    scoring.write("Player A: {} --- Player B: {}".format(ball.aScore,ball.bScore), move=False, align='center', font=('arial', 15, 'normal'))
    
    screen.listen()
    screen.onkeypress(paddleA.paddleUp, 'w')
    screen.onkeypress(paddleB.paddleUp, "Up")
    screen.onkeypress(paddleA.paddleDown, 's')
    screen.onkeypress(paddleB.paddleDown, 'Down')

    while run:
        screen.update()
        ball.moveBall()
        ball.borderCheck()
        ball.collisions()

class A_Paddle:

    def __init__(self, x, y):
        self.paddle = turtle.Turtle()
        self.paddle.color('white')
        self.paddle.speed(0)
        self.paddle.shape('square')
        self.paddle.shapesize(stretch_wid=5,stretch_len=1)
        self.paddle.penup()
        self.paddle.setpos(x, y)

    def paddleUp(self):
        y = self.paddle.ycor()
        y += 20
        self.paddle.sety(y)

    def paddleDown(self):
        y = self.paddle.ycor()
        y -= 20
        self.paddle.sety(y)

class Ball:
    def __init__(self):
        self.ball = turtle.Turtle()
        self.ball.penup()
        self.ball.color('white')
        self.ball.speed(0)
        self.ball.shape('circle')
        self.x_velocity = 4
        self.y_velocity = 4
        self.aScore = 0
        self.bScore = 0

    def moveBall(self):
        self.ball.setx(self.ball.xcor() + self.x_velocity)
        self.ball.sety(self.ball.ycor() + self.y_velocity)

    def borderCheck(self):
        if self.ball.ycor() >= HEIGHT // 2 - 12  or self.ball.ycor() <= HEIGHT // -2 + 20:
            self.y_velocity *= -1
        if self.ball.xcor() >= WIDTH // 2 + 10:
            self.aScore += 1
            scoring.clear()
            scoring.write("Player A: {} --- Player B: {}".format(ball.aScore,ball.bScore), move=False, align='center', font=('arial', 15, 'normal'))
            self.ball.home()
            self.x_velocity *= -1
        if self.ball.xcor() <= WIDTH // -2 - 10:
            self.bScore += 1
            scoring.clear()
            scoring.write("Player A: {} --- Player B: {}".format(ball.aScore,ball.bScore), move=False, align='center', font=('arial', 15, 'normal'))
            self.ball.home()
            self.x_velocity *= -1

    def collisions(self):
        if self.ball.xcor() < WIDTH // -2 + 50 and self.ball.ycor() < paddleA.paddle.ycor() + 50 and self.ball.ycor() > paddleA.paddle.ycor() - 50:
            ball.x_velocity *= -1
        elif self.ball.xcor() > WIDTH // 2 - 56 and self.ball.ycor() < paddleB.paddle.ycor() + 50 and self.ball.ycor() > paddleB.paddle.ycor() - 50:
            ball.x_velocity *= -1


paddleA = A_Paddle(WIDTH // -2 + 30, 0)
paddleB = A_Paddle(WIDTH // 2 - 36, 0)
ball = Ball()

showScreen()
