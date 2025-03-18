import turtle

# game screen

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=650)
wn.tracer(0)

welcome = turtle.Turtle()
player_a = turtle.Turtle()
player_b = turtle.Turtle()
ball = turtle.Turtle()
a_score = 0
b_score = 0
score = turtle.Turtle()
border = turtle.Turtle()


def welcomeScreen():
    # welcome screen
    welcome.hideturtle()
    welcome.speed(0)
    welcome.penup()
    welcome.color("white")  # Added this line to ensure text is visible
    welcome.goto(0, 100)  # Changed position for better visibility
    welcome.write("WELCOME TO PONG!", align="center", font=("Courier", 36, "normal"))
    welcome.goto(0, 0)  # Changed position
    welcome.write("Player A: W for UP, S for DOWN", align="center", font=("Courier", 20, "normal"))
    welcome.goto(0, -50)  # Changed position
    welcome.write("Player B: ARROW UP for UP, ARROW DOWN for DOWN", align="center", font=("Courier", 20, "normal"))
    welcome.goto(0, -120)  # Added instruction
    welcome.write(
        "Press ENTER to start the game", align="center", font=("Courier", 16, "normal")
    )
    wn.update()


def startGame():
    
    if welcome:
        try:
            welcome.hideturtle()
            welcome.clear()
        except:
            pass  # Avoid error if welcome is already removed
    print("game should've started")   
    # player a
    player_a.speed(0)
    player_a.penup()
    player_a.shape("square")
    player_a.color("white")
    player_a.shapesize(stretch_wid=6, stretch_len=1)
    player_a.setx(-350)
    player_a.sety(0)

    # player b

    player_b.speed(0)
    player_b.penup()
    player_b.shape("square")
    player_b.color("white")
    player_b.shapesize(stretch_wid=6, stretch_len=1)
    player_b.setx(350)
    player_b.sety(0)

    # ball

    ball.speed(0)
    ball.penup()
    ball.shape("square")
    ball.color("white")
    ball.setx(0)
    ball.sety(0)
    ball.dx = 0.18
    ball.dy = 0.18

    # scoreboard
    score.speed(0)
    score.penup()
    score.color("white")
    score.shape("square")
    score.hideturtle()

    # initial scoreboard
    score.goto(-280, 270)
    score.write(f"Player A: {a_score}", align="center", font=("Courier", 24, "normal"))
    score.goto(280, 270)
    score.write(f"Player B: {b_score}", align="center", font=("Courier", 24, "normal"))

    # border line
    border.speed(0)
    border.color("white")
    border.hideturtle()
    border.penup()
    border.goto(-400, 260)
    border.pendown()
    border.setx(400)
