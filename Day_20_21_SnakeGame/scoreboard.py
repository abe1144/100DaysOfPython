from turtle import Turtle
import os


class Scoreboard(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.score = 0

        with open("data.txt") as f:
            self.high_score = int(f.read())
        self.penup()
        self.color("white")
        self.setposition(0, 280)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write("Score: {} High Score:{}".format(self.score, self.high_score),
                   align="center", font=("Arial", 12))

    # def game_over(self):
    #     self.setposition(0, 0)
    #     self.write("Game Over", align="center", font=("Arial", 12))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as f:
                f.write(str(self.high_score))
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()
