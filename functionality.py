import actors


game_start = False

a = actors.player_a
b = actors.player_b
score = actors.score
#welcome = actors.welcome

#def welcomeScreen():

def gameState():
    global game_start
    game_start = True
    print("game started daddy!")

def a_up():
    if(a.ycor() < 200):
        a.sety(a.ycor() + 0.75)


def a_down():
    if(a.ycor() > -260):
        a.sety(a.ycor() - 0.75)


def b_up():
    if(b.ycor() < 200):
        b.sety(b.ycor() + 0.75)


def b_down():
    if(b.ycor() > -260):
        b.sety(b.ycor() - 0.75)


# score update
def scoreUpdate():
    score.clear()
    score.goto(-280, 270)
    score.write(f"Player A: {actors.a_score}", align="center", font=("Courier", 24, "normal"))
    score.goto(280, 270)
    score.write(f"Player B: {actors.b_score}", align="center", font=("Courier", 24, "normal"))
