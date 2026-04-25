from turtle import Turtle

FONT = ("Courier", 19, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.write(arg=f"Level = {self.level}", align='left', font=FONT)

    def change_level(self):
        self.level += 1
        self.clear()
        self.write(arg=f"Level = {self.level}", align='left', font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(arg="Game Over.", align='center', font=FONT)

