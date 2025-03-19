# Day-18-Turtle-Graphics
Turtle Graphics - Difficulty: Easy

## Author:
Carlos Valerio (CarlosValerioM)

## Date:
2025/03/19

## License:
MIT License

## Dependencies:
- Python (built-in library `turtle`)
- Random (built-in library)

## Description:
`turtle_graphics.py` is a simple Python script that uses the `turtle` module to create random-colored dots in a grid pattern. The script moves the turtle across the screen and places dots at regular intervals, changing the color of each dot randomly.

The user can observe the turtle moving and drawing dots on the screen, with the size and color of the dots being randomized for a fun visual effect.

## Usage:

1. Clone this repository:

```bash
git clone https://github.com/CarlosValerioM/Day-2-Turtle-Graphics.git
```
Navigate to the project directory:

```bash
cd Day-2-Turtle-Graphics
```
Run the script:

```bash
python turtle_graphics.py
```
The script will start drawing a grid of random-colored dots using the turtle.

Example Output:
1. A window will appear showing a grid of dots of random colors, created by the turtle.
2. The turtle will start from the coordinates (-100, -100) and draw dots at intervals of 50 pixels, creating a grid-like pattern.
3. How it works:
4. The turtle starts at a predefined location (x = -100, y = -100).
5. It moves in steps, drawing dots of random colors at each position.
6. The size of each dot is fixed at 20 pixels.
7. The turtle continues to draw the grid until it reaches the designated size.
8. The script uses the turtle's forward method to move, dot to draw the dots, and random colors are generated using the random.randint() function.

License:
This project is licensed under the MIT License.
