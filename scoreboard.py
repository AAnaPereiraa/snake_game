from turtle import Turtle

FONT = ('Arial', 12, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 280)
        self.score = 0
        self.score_count()
        
    def score_count(self):
        self.clear()
        self.write(f"Score = {self.score}", align="center", font=FONT)
        self.score += 1
    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

    def reset(self):
        self.score = 0
        self.goto(0, 280)
        self.score_count()
        
        
        
        