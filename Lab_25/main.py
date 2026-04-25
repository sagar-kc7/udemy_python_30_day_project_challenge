import turtle
import pandas as pd

screen = turtle.Screen()
screen.title('U.S. States game')
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_df = pd.read_csv('50_states.csv')
state = states_df['state'].to_list()
guessed_state = []

while len(guessed_state) <50:
    answer = screen.textinput(title=f'{len(guessed_state)}/50 states correct',
                              prompt="Whats another state name?").title()

    if answer == 'Exit':
        break

    if answer in state:
        guessed_state.append(answer)
        tim =turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        state_detail = states_df[states_df['state'] == answer]
        tim.goto(state_detail['x'].item(), state_detail['y'].item())
        tim.write(answer)

screen.exitonclick()