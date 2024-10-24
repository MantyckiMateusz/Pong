from turtle import Turtle

class Player(Turtle):
    #initialize player on starting position
    def __init__(self, starting_pos, games_speed, screen_heigth):
        super().__init__()
        
        self.speed = games_speed
        self.screen_height = screen_heigth
        
        self.penup()
        self.shape('square')
        self.setheading(90)
        self.shapesize(stretch_len=3)
        self.goto(starting_pos)
        self.color('white')

    #up/down movement
    def move_up(self):
        if self.ycor() < ((self.screen_height/2) - 40):
            self.forward(self.speed)

    def move_down(self):
        if self.ycor() > ((self.screen_height/-2) + 40):
            self.back(self.speed)
