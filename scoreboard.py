from turtle import Turtle
ALIGNMENT = "center"
FONT = "Courier"


class ScoreBoard(Turtle):
    def __init__(self,score):
        super().__init__()
        self.score = 0
        self.high_score =score
        self.color("white")
        self.hideturtle()
        self.up()
        self.goto(0,280)
        self.write(f"Score : {self.score} highscore: {self.high_score}",align="center",font=('Arial', 12, 'bold'))

    def increase_score(self):
        self.clear()
        self.score+=1
        self.write(f"Score : {self.score} HighScore:{self.high_score  }",align=ALIGNMENT,font=(FONT, 12, 'bold'))

        # def game_over(self):
    #     self.color("yellow")
    #     self.goto(0,0)
    #     self.write(f"GAME OVER",align=ALIGNMENT,font=(FONT, 20, 'bold'))

    def reset_scoreboard(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("data.txt",mode="w") as file:
                file.write(str(self.high_score))
                
        self.score =0
        self.increase_score()