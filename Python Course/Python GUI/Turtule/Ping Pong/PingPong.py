import turtle
import winsound

class WindowScreen:
    # Display window to screen
    Window = turtle.Screen()

    # Title App
    Window.title("Ping Pong by @Dhruv0705")

    # Set background color to black
    Window.bgcolor("black")

    # Screen Size
    Window.setup(width=800, height=600)

    # Accelerate drawing
    Window.tracer(0)
    
class Score:

    # Sets PlayerA and Player B score to 0 as a counter element
    PlayerAScore = 0
    PlayerBScore = 0

class Paddle:
    class LeftPaddle:
        
        # Draws left paddle
        LEFTPaddle = turtle.Turtle()
        LEFTPaddle.speed(2)
        LEFTPaddle.shape('square')
        LEFTPaddle.color('white')
        LEFTPaddle.shapesize(stretch_wid=5, stretch_len=1)
        LEFTPaddle.penup()
        LEFTPaddle.goto(-350, 0)

        def MoveLeftPaddleUp():
            # Return y coordinate to variable
            y = Paddle.LeftPaddle.LEFTPaddle.ycor()
            # Add 20 pixel to y coordinate
            y +=20
            
            # Set y to the new y variable
            Paddle.LeftPaddle.LEFTPaddle.sety(y)
        
        def MoveLeftPaddleDown():
            # Return y coordinate to variable
            y = Paddle.LeftPaddle.LEFTPaddle.ycor()
            # Minus 20 pixel to y coordinate (Move box down)
            y -=20
            
            # Set y to the new y variable
            Paddle.LeftPaddle.LEFTPaddle.sety(y)
        # Keyboard binding
        # Window Listener()
        WindowScreen.Window.listen()
        
        # Calls the function when user presses w or s
        WindowScreen.Window.onkeypress(MoveLeftPaddleUp, "w")
        WindowScreen.Window.onkeypress(MoveLeftPaddleDown, "s")

    class RightPaddle:
        RIGHTPaddle = turtle.Turtle()
        RIGHTPaddle.speed(0)
        RIGHTPaddle.shape('square')
        RIGHTPaddle.color('white')
        RIGHTPaddle.shapesize(stretch_wid=5, stretch_len=1)
        RIGHTPaddle.penup()
        RIGHTPaddle.goto(350, 0)

        # Move Paddle Function
        def MoveRightPaddleUp():
            # Return y coordinate to variable
            y = Paddle.RightPaddle.RIGHTPaddle.ycor()
            # Add 20 pixel to y coordinate
            y +=20
            
            # Set y to the new y variable
            Paddle.RightPaddle.RIGHTPaddle.sety(y)
        
        def MoveRightPaddleDown():
            # Return y coordinate to variable
            y = Paddle.RightPaddle.RIGHTPaddle.ycor()
            # Minus 20 pixel to y coordinate (Move box down)
            y -=20
            
            # Set y to the new y variable
            Paddle.RightPaddle.RIGHTPaddle.sety(y)

    # Calls the function when user presses arrow key up or down
        WindowScreen.Window.onkeypress(MoveRightPaddleUp, "Up")
        WindowScreen.Window.onkeypress(MoveRightPaddleDown, "Down")

class Ball:
    # Ball
    BALL = turtle.Turtle()
    BALL.speed(0)
    BALL.shape( 'circle')
    BALL.color('white')
    BALL.penup()
    BALL.goto(0, 0)

# Separate ball movement in two parts x and y to 
Ball.BALL.dx = 0.1
Ball.BALL.dy = 0.1

class Pen:

    PEN = turtle.Turtle()
    PEN.speed(0)
    PEN.shape("square")
    PEN.color("white")
    PEN.penup()
    PEN.hideturtle()
    PEN.goto(0, 260)
    PEN.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Main game loop
while True:

    # Update to screen
    WindowScreen.Window.update()

    # Move Ball
    # Set Ball x and y coordinates as ((x coordinates) + (Ball.dx value))
    Ball.BALL.setx(Ball.BALL.xcor() + Ball.BALL.dx)
    Ball.BALL.sety(Ball.BALL.ycor() + Ball.BALL.dy)
    # Top and bottom
    if Ball.BALL.ycor() > 290:
        Ball.BALL.sety(290)
        Ball.BALL.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    
    elif Ball.BALL.ycor() < -290:
        Ball.BALL.sety(-290)
        Ball.BALL.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # Left and right
    if Ball.BALL.xcor() > 350:
        Score.PlayerAScore += 1
        Pen.PEN.clear()
        Pen.PEN.write("Player A: {}  Player B: {}".format(Score.PlayerAScore, Score.PlayerBScore), align="center", font=("Courier", 24, "normal"))
        Ball.BALL.goto(0, 0)
        Ball.BALL.dx *= -1

    elif Ball.BALL.xcor() < -350:
        Score.PlayerBScore += 1
        Pen.PEN.clear()
        Pen.PEN.write("Player A: {}  Player B: {}".format(Score.PlayerAScore, Score.PlayerBScore), align="center", font=("Courier", 24, "normal"))
        Ball.BALL.goto(0, 0)
        Ball.BALL.dx *= -1

    # Paddle and ball collisions
    if Ball.BALL.xcor() < -340 and Ball.BALL.ycor() <  Paddle.LeftPaddle.LEFTPaddle.ycor() + 50 and Ball.BALL.ycor() >  Paddle.LeftPaddle.LEFTPaddle.ycor() - 50:
        Ball.BALL.dx *= -1.03 
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    
    elif Ball.BALL.xcor() > 340 and Ball.BALL.ycor() < Paddle.RightPaddle.RIGHTPaddle.ycor() + 50 and Ball.BALL.ycor() > Paddle.RightPaddle.RIGHTPaddle.ycor() - 50:
        Ball.BALL.dx *= -1.03
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
