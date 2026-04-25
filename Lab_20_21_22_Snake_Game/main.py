from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

WIDTH = 600
HEIGHT = 600

# Screen setup
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("My snake game....")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.update()
screen.listen()

screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")
screen.onkey(snake.left, "a")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.07)
    snake.move()

    if snake.head.distance(food) <15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()