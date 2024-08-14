from turtle import Turtle

# Font style for scoreboard text
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0  # Initial score
        self.color("black")
        self.penup()
        self.goto(180, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        # Display the current score
        self.write(f"Level: {self.points}", align="center", font=FONT)

    def increase_score(self):
        # Increment the score and update display
        self.points += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        # Display the game over message
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
