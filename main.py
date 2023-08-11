import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


state_data = pandas.read_csv("50_states.csv")
all_states = state_data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    ans_state = screen.textinput(title="Guess the state", prompt=f"Correct: {len(guessed_states)}/50").title()
    ans_state_data = state_data[state_data.state == ans_state]
    if ans_state == "Exit":
        remaining_states = [state for state in all_states if state not in guessed_states]
        df = pandas.DataFrame(remaining_states)
        df.to_csv("remaining_states.csv")
        break
    if ans_state in all_states:
        guessed_states.append(ans_state)
        columbus = turtle.Turtle()
        columbus.hideturtle()
        columbus.penup()
        x_coordinate = int(ans_state_data.x)
        y_coordinate = int(ans_state_data.y)
        columbus.goto(x_coordinate, y_coordinate)
        columbus.write(f"{ans_state}", font=("Arial", 8, "normal"), align="center")