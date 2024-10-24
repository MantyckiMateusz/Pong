from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, font, net_heigth):
        super().__init__()
        
        self.score_player_1 = 0
        self.score_player_2 = 0
        self.net_heigth = net_heigth
        self.font = font
        
        self.hideturtle()
        self.drawn_net()
        self.write_score()

    #Draw the "net" in the middle of the screen
    def drawn_net(self):
        self.goto(0, -300)
        self.penup()
        self.pensize(width=5)
        self.shape('square')
        self.goto(0, -300)
        self.setheading(90)
        self.color('white')
        for i in range(30):
            self.pendown()
            self.fd(self.net_heigth)
            self.penup()
            self.fd(self.net_heigth)

    #Write score on screen
    def write_score(self):
        self.penup()
        self.goto(-30, 260)
        self.write(self.score_player_1, False, font=self.font)
        self.goto(20, 260)
        self.write(self.score_player_2, False, font=self.font)
 
    #Increase score
    def increase_score(self, player_number):
        """Increases score for specified player

        Args:
            player_number (int): Player number of the player that scored the point, takes either 1 for player_1 or 2 for player_2

        Raises:
            ValueError: Raised for any player_number value other than 1 or 2
        """

        if player_number == 1:
            self.score_player_1 += 1
        elif player_number == 2:
            self.score_player_2 += 1
        else:
            raise ValueError('Wrong value for player_number, expected 1 or 2')
        
        self.clear()
        self.drawn_net()
        self.write_score()
        
    def game_over(self):
        winner = 'Player 1' if self.score_player_1 > self.score_player_2 else 'Player 2'

        self.clear()
        self.goto(0,0)
        self.write(winner + ' wins!', align='center', font=self.font)