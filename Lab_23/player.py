from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.left(90)
        self.start_line()
        self.shape("turtle")

    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(0, new_y)

    def start_line(self):
        self.goto(STARTING_POSITION)

    def at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False