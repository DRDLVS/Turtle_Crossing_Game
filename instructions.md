## Turtle Game Instructions

### 1. Create a Turtle Player
- The turtle player should start at the bottom of the screen.
- Listen for the "Up" keypress to move the turtle north.
- If you get stuck, check the video walkthrough in **Step 3**.

### 2. Create Cars
- Cars should be 20px high by 40px wide.
- They should be randomly generated along the y-axis and move towards the left edge of the screen.
- No cars should be generated in the top and bottom 50px of the screen (consider these as safe zones for the turtle).
- **Hint:** Generate a new car only every 6th time the game loop runs.
- If you get stuck, check the video walkthrough in **Step 4**.

### 3. Detect Collisions
- Detect when the turtle player collides with a car and stop the game if this happens.
- If you get stuck, check the video walkthrough in **Step 5**.

### 4. Detect Successful Crossings
- Detect when the turtle player reaches the top edge of the screen (i.e., the `FINISH_LINE_Y`).
- When this happens:
  - Return the turtle to the starting position.
  - Increase the speed of the cars.
- **Hint:** Consider creating an attribute and using the `MOVE_INCREMENT` to increase car speed.
- If you get stuck, check the video walkthrough in **Step 6**.

### 5. Create a Scoreboard
- Track the level the user is on.
- Increase the level every time the turtle successfully crosses the screen.
- When the turtle hits a car, display "GAME OVER" in the center.
- If you get stuck, check the video walkthrough in **Step 7**.
