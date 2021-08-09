from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.penup()
        self.shape("turtle")
        self.reset_position()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def is_at_end(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
