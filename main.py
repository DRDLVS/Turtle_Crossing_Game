import time
from turtle import Screen
from player import Player, STARTING_POSITION
from car_manager import CarManager
from scoreboard import Scoreboard

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)  # Turn off animation for smoother updates

# Create instances of Player, CarManager, and Scoreboard
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Set up key listener for player movement
screen.listen()
screen.onkeypress(player.up, "Up")

# Main game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)  # Control the game loop speed
    screen.update()  # Update the screen

    # Create new cars and move existing cars
    car_manager.create_car()
    car_manager.move_cars()

    # Check for collisions with cars
    for car in car_manager.all_cars:
        if player.distance(car) < 25:
            scoreboard.game_over()
            game_is_on = False

    # Check if player has reached the finish line
    if player.ycor() > 290:
        car_manager.increase_speed()
        player.goto(STARTING_POSITION)
        scoreboard.increase_score()

# Close the screen on click
screen.exitonclick()
