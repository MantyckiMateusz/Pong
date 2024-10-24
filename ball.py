from random import choice
from turtle import Turtle

class Ball(Turtle):
    def __init__(self, game_speed):
        super().__init__()
        
        self.speed = game_speed / 2
        
        self.shape('circle')
        self.penup()
        self.color('white')
        self.respawn()

    #move the ball with every tick of the game loop
    def move(self):
        self.forward(self.speed)

    #Change the ball direction on collision
    def change_direction(self):
        self.setheading(315 if self.heading() - 90 < 0 else self.heading() - 90)
        
    #Move the ball to the middle of the screen after it gets out of bounds
    def respawn(self):
        self.goto(0,0)
        self.setheading(choice([45, 135, 225, 315]))