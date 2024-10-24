import time
from turtle import Screen
from player import Player
from ball import Ball
from scoreboard import Scoreboard

#Config values
TITLE = "Pong Game"
SCREEN_SIZE = [600, 600]
GAME_SPEED = 30
GAME_SCORE_LIMIT = 5 
NET_LINE_HEIGHT = 20
FONT = ('Cascadia Code', 20,  'bold')

#Screen config
screen = Screen()
screen.setup(width=SCREEN_SIZE[0], height=SCREEN_SIZE[1])
screen.bgcolor('black')
screen.tracer(0)
screen.title(TITLE)

#Init players, the ball and the scoreboard
player_1_starting_x = (SCREEN_SIZE[0]/-2)+20
player_2_starting_x = (SCREEN_SIZE[0]/2)-20

player_1 = Player((player_1_starting_x, 0), GAME_SPEED, SCREEN_SIZE[1])
player_2 = Player((player_2_starting_x, 0), GAME_SPEED, SCREEN_SIZE[1])
ball = Ball(GAME_SPEED)
scoreboard = Scoreboard(FONT, NET_LINE_HEIGHT)

#Listen for keys
screen.listen()
screen.onkeypress(player_1.move_up, "w")
screen.onkeypress(player_1.move_down, "s")
screen.onkeypress(player_2.move_up, "Up")
screen.onkeypress(player_2.move_down, "Down")

#Main game loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    #Detect collision with walls and player
    if ball.ycor() > 280 or ball.ycor() < -280 or ball.distance(player_1) < 20 or ball.distance(player_2) < 20:
        ball.change_direction()

    #Detect out of bounds
    if ball.xcor() > 280:
        scoreboard.increase_score(1)
        ball.respawn()

    if ball.xcor() < -280:
        scoreboard.increase_score(2)
        ball.respawn()   

    #Detect game over
    if scoreboard.score_player_1 == 5 or scoreboard.score_player_2 == 5:
        scoreboard.game_over()
        game_is_on = False

    ball.move()
#Keep screen from closing automaticaly
screen.exitonclick()
