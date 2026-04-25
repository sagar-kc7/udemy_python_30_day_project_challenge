from turtle import Turtle, Screen

screen = Screen()
screen.setup(width= 700, height= 500)
user_bet = screen.textinput(title="Make your bet", prompt='Choose your color.')
colors = ['red', 'green', 'blue', 'yellow', 'black', 'purple']
turtle_position = [-150, -90, -30, 30, 90, 150]

for turtle_index in range(0, 6):
    tim = Turtle(shape='turtle')
    tim.penup()
    tim.color(colors[turtle_index])
    tim.goto(x=-325, y=turtle_position[turtle_index])





screen.exitonclick()