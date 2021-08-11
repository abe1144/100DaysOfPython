import pandas as pd
import turtle
states_data = pd.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("U.S. States Game")

screen.addshape("blank_states_img.gif")

turtle.shape("blank_states_img.gif")


states = states_data['state'].str.lower().tolist()

guessed_states = []

label = turtle.Turtle()
label.penup()
label.hideturtle()

while len(guessed_states) < 50:
    if len(guessed_states) == 0:
        answer_state = screen.textinput(
            title="Guess the State", prompt="What's another state name?")

    else:
        answer_state = screen.textinput(
            title="{}/50 Correct".format(len(guessed_states)), prompt="What's another state name?")

    if answer_state.title() in states_data['state'].tolist():
        row = states_data[states_data['state'] == answer_state.title()]

        # filter df
        x = row.x.values[0]
        y = row.y.values[0]

        label.goto(x, y)
        label.write(row.state.values[0])
        guessed_states.append(row.state.values[0])

    elif answer_state.title() == "Exit":
        not_guessed = states_data[~states_data.state.isin(guessed_states)]
        not_guessed.to_csv('states_to_learn.csv', index=False)
        break
