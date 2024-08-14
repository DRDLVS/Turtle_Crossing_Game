from turtle import Turtle
import random

# Colors available for cars
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
# Initial speed of cars
STARTING_MOVE_DISTANCE = 5
# Speed increment for cars
MOVE_INCREMENT = 3


class CarManager:
    def __init__(self):
        # Initialize the list of cars, speed, and loop counter
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.loop_counter = 0

    def create_car(self):
        # Increment the loop counter
        self.loop_counter += 1

        # Create a new car every 6 loops
        if self.loop_counter % 6 == 0:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        # Move all cars leftward by the current speed
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        # Increase the speed of the cars
        self.car_speed += MOVE_INCREMENT




