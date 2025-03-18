# TODO: Make Timer System
#       FPS Meter


import os
import actors
import functionality
import random


wn = actors.wn

actors.welcomeScreen()
#os.system("aplay mountain-trials.mp3&")

# Track key states
key_states = {"w": False, "s": False, "Up": False, "Down": False}


# Key press and release handlers
def key_down(key):
    key_states[key] = True


def key_up(key):
    key_states[key] = False


# Set up key listeners
wn.listen()
wn.onkeypress(lambda: key_down("w"), "w")
wn.onkeyrelease(lambda: key_up("w"), "w")
wn.onkeypress(lambda: key_down("s"), "s")
wn.onkeyrelease(lambda: key_up("s"), "s")
wn.onkeypress(lambda: key_down("Up"), "Up")
wn.onkeyrelease(lambda: key_up("Up"), "Up")
wn.onkeypress(lambda: key_down("Down"), "Down")
wn.onkeyrelease(lambda: key_up("Down"), "Down")

wn.onkeypress(functionality.gameState, "Return")


ball = actors.ball
player_a = actors.player_a
player_b = actors.player_b

while not functionality.game_start:
    # print("welcome screen should be there")
    wn.update()

#os.system("killall afplay")
actors.startGame()
#os.system("aplay power-up.mp3&")
# game loop

while functionality.game_start:
    wn.update()

    # Handle paddle movement based on key states
    if key_states["w"]:
        functionality.a_up()
    if key_states["s"]:
        functionality.a_down()
    if key_states["Up"]:
        functionality.b_up()
    if key_states["Down"]:
        functionality.b_down()

    # move ball

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # top and bottom walls

    if ball.ycor() > 250:
        ball.sety(250)
        ball.dy *= -1
        os.system("aplay wall-hit.wav&")

    elif ball.ycor() < -310:
        ball.sety(-310)
        ball.dy *= -1
        os.system("aplay wall-hit.wav&")

    # left and right border

    if ball.xcor() > 390:
        ball.setposition(0,0)
        ball.dx *= -1
        actors.a_score += 1
        functionality.scoreUpdate()
        os.system("aplay score.wav&")

    elif ball.xcor() < -390:
        ball.setposition(0,0)
        ball.dx *= -1
        actors.b_score += 1
        functionality.scoreUpdate()
        os.system("aplay score.wav&")

    # paddle collision

    if (ball.xcor() <= player_a.xcor() + 10) and (ball.xcor() >= player_a.xcor() - 10):
        if (ball.ycor() <= player_a.ycor() + 60) and (ball.ycor() >= player_a.ycor() - 60):
            ball.setx(player_a.xcor() + 10)  # Prevent ball from getting stuck
            ball.dx *= -1
            ball.dx += random.choice([-0.01, 0.01])
            os.system("aplay paddle-hit.wav&")

    if (ball.xcor() <= player_b.xcor() + 10) and (ball.xcor() >= player_b.xcor() - 10):
        if (ball.ycor() <= player_b.ycor() + 60) and (ball.ycor() >= player_b.ycor() - 60):
            ball.setx(player_b.xcor() - 10)  # Prevent ball from getting stuck
            ball.dx *= -1
            ball.dx += random.choice([-0.01, 0.01])
            os.system("aplay paddle-hit.wav&")
