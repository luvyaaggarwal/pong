# TODO: Make Timer System
#       FPS Meter


import winsound
import actors
import functionality
import random
import time


wn = actors.wn

actors.welcomeScreen()
# os.system("aplay mountain-trials.mp3&")

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

# os.system("killall afplay")
actors.startGame()
# os.system("aplay power-up.mp3&")
# game loop

last_time = time.time()
frame_count = 0

while functionality.game_start:
    wn.update()
    frame_count += 1
    current_time = time.time()
    elapsed_time = current_time - last_time

    if elapsed_time >= 0.5:
        fps = frame_count / elapsed_time
        actors.fps_display.clear()
        actors.fps_display.write(f"FPS: {fps:.2f}", align="left", font=("Courier", 16, "normal"))
        frame_count = 0
        last_time = current_time

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
        winsound.PlaySound("wall-hit.wav", winsound.SND_ASYNC)

    elif ball.ycor() < -310:
        ball.sety(-310)
        ball.dy *= -1
        winsound.PlaySound("wall-hit.wav", winsound.SND_ASYNC)

    # left and right border

    if ball.xcor() > 390:
        ball.setposition(0, 0)
        ball.dx *= -1
        actors.a_score += 1
        functionality.scoreUpdate()
        winsound.PlaySound("score.wav", winsound.SND_ASYNC)

    elif ball.xcor() < -390:
        ball.setposition(0, 0)
        ball.dx *= -1
        actors.b_score += 1
        functionality.scoreUpdate()
        winsound.PlaySound("score.wav", winsound.SND_ASYNC)

    # paddle collision

    if (ball.xcor() <= player_a.xcor() + 10) and (ball.xcor() >= player_a.xcor() - 10):
        if (ball.ycor() <= player_a.ycor() + 60) and (
            ball.ycor() >= player_a.ycor() - 60
        ):
            ball.setx(player_a.xcor() + 10)  # Prevent ball from getting stuck
            ball.dx *= -1
            ball.dx += random.choice([-0.01, 0.01])
            winsound.PlaySound("paddle-hit.wav", winsound.SND_ASYNC)

    if (ball.xcor() <= player_b.xcor() + 10) and (ball.xcor() >= player_b.xcor() - 10):
        if (ball.ycor() <= player_b.ycor() + 60) and (
            ball.ycor() >= player_b.ycor() - 60
        ):
            ball.setx(player_b.xcor() - 10)  # Prevent ball from getting stuck
            ball.dx *= -1
            ball.dx += random.choice([-0.01, 0.01])
            winsound.PlaySound("paddle-hit.wav", winsound.SND_ASYNC)
