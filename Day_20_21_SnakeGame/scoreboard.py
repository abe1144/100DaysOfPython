from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0
        Turtle.__init__(self)
        self.penup()
        self.color("white")
        self.setposition(0, 280)
        self.hideturtle()
        self.write("Score: {}".format(self.score),
                   align="center", font=("Arial", 12))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write("Score: {}".format(self.score),
                   align="center", font=("Arial", 12))

    def game_over(self):
        self.setposition(0, 0)
        self.write("Game Over", align="center", font=("Arial", 12))
