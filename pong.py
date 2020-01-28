import turtle

window = turtle.Screen()
window.title('Pong')
window.bgcolor('black')
window.setup(width = 800, height = 600)
#tracer is meant to speed up the game
window.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.color('white')
paddle_a.shape('square')
paddle_a.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0, 0)
# d - delta -- change
ball.dx = 0.5
ball.dy = 0.5

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('Player A : 0 Player B : 0', move = False, align = 'center', font = ('Courier', 16,'normal'))

def paddle_a_up():
    y = paddle_a.ycor()
    y = y + 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y = y - 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y = y + 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y = y - 20
    paddle_b.sety(y)

# Keyboard Binding
window.listen()
# Paddle A
window.onkeypress(paddle_a_up, 'w')
window.onkeypress(paddle_a_down, 's')
# Paddle B
window.onkeypress(paddle_b_up, 'Up')
window.onkeypress(paddle_b_down, 'Down')

# Game loop
while True:
    window.update()
    
    # Ball Movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy = ball.dy * -1
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy = ball.dy * -1
        
    if ball.xcor() > 395:
        ball.goto(0, 0)
        ball.dx = ball.dx * -1
        score_a = score_a + 1
        pen.clear()
        pen.write('Player A : {} Player b : {}'.format(score_a, score_b), move = False, align = 'center', font = ('Courier', 16, 'normal'))
        
    if ball.xcor() < -395:
        ball.goto(0, 0)
        ball.dx = ball.dx * -1
        score_b = score_b + 1
        pen.clear()
        pen.write('Player A : {} Player b : {}'.format(score_a, score_b), move = False, align = 'center', font = ('Courier', 16, 'normal'))

        
    # Paddle and Ball Collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx = ball.dx * -1
        
    if (ball.xcor() > -350 and ball.xcor() < -340) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx = ball.dx * -1
    
## For sound effects
    ## import winsound
    ## winsound.PlaySound('name of the audio_file', winsound.SND_ASYNC)