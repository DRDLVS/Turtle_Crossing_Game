# Turtle Crossing Game

## Overview

The Turtle Crossing Game is a simple Python game built using the `turtle` graphics module. The player controls a turtle that must cross a busy road filled with cars moving horizontally across the screen. The goal is to reach the top of the screen without colliding with any of the cars. Each successful crossing increases the game level, making the cars move faster.

## Features

- **Player Control**: The turtle is controlled by the player using the "Up" key to move forward (north).
- **Car Generation**: Cars are randomly generated on the right side of the screen and move to the left. The number and speed of cars increase with each level.
- **Collision Detection**: If the turtle collides with a car, the game ends and displays a "Game Over" message.
- **Level Progression**: Each time the turtle successfully reaches the top of the screen, the level increases, and the cars' speed increases accordingly.
- **Scoreboard**: Displays the current level of the player. The score increases by one for each successful crossing.

## Project Structure

- **main.py**: The main script that runs the game loop, manages user input, and handles game logic such as car creation, movement, collision detection, and level progression.
- **player.py**: Contains the `Player` class, which represents the turtle controlled by the player.
- **car_manager.py**: Contains the `CarManager` class, responsible for generating and moving cars on the screen.
- **scoreboard.py**: Contains the `Scoreboard` class, which keeps track of the player’s level and displays the score and game over message.

## How to Play

1. Run the `main.py` script to start the game.
2. Use the "Up" arrow key to move the turtle upwards.
3. Avoid getting hit by cars as you move towards the top of the screen.
4. Each time you reach the top, the game level increases, and cars move faster.
5. The game ends when the turtle collides with a car, displaying a "Game Over" message.
