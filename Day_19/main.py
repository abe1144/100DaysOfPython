import turtle as t
import random

is_race_on = False
screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

for i in range(len(colors)):
    turtle = t.Turtle(shape="turtle")
    turtle.penup()
    turtle.color(colors[i])
    # turtles.append(turtle)
    turtle.goto(x=-230, y=-100 + i * 30)
    all_turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You've won! The {} turtle is the winner!".format(winning_color))
            else:
                print("You lose! The {} turtle is the winner!".format(winning_color))
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
