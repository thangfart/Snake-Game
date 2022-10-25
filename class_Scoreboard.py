from turtle import Turtle
from Exercises.day24.main import write_new_record,read_new_record
PATH = "data.txt"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highest_score = int(read_new_record(PATH))
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.updateScoreboard()

    def updateScoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} & Highest Score: {self.highest_score}",align='right',font=("Arial",14,"normal"))
        write_new_record(PATH,str(self.highest_score))

    def resetSb(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
        self.score = 0
        #self.highest_score = 0
        self.updateScoreboard()

    """def printGameOver(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align='center',font=("Arial",44,"normal"))"""

    """def incHighestScore(self):
        self.highest_score += 1
        self.updateScoreboard()"""

    def incScore(self):
        self.score += 1
        #self.highest_score += 1
        self.updateScoreboard()



