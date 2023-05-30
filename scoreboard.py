from turtle import Turtle
ALIGNMENT = "center"
FONT = "Courier"
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.up()
        self.goto(0,280)
        self.write(f"Score : {self.score}",align="center",font=('Arial', 12, 'bold'))

    def increase_score(self):
        self.clear()
        self.score+=1
        self.write(f"Score : {self.score}",align=ALIGNMENT,font=(FONT, 12, 'bold'))

    def game_over(self):
        self.color("yellow")
        self.goto(0,0)
        self.write(f"GAME OVER",align=ALIGNMENT,font=(FONT, 20, 'bold'))