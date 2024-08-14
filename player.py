from turtle import Turtle

# Constants for player positioning and movement
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        # Initialize the player turtle
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def up(self):
        # Move the player turtle forward
        self.forward(MOVE_DISTANCE)
