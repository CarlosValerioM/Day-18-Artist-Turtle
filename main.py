#!/usr/bin/env python3
"""
turtle_painter.py - A script that uses Python's Turtle module to draw random-colored dots in a grid pattern.

Author: Carlos Valerio (CarlosValerioM)
Date: 2025/03/19
License: MIT
Dependencies: turtle (built-in Python library)

Description:
This script uses the Turtle module to draw a grid of random-colored dots. The turtle starts at a specified position and moves across the screen, drawing dots as it goes. The grid is created based on a fixed size and step movement for both X and Y coordinates. Each dot is drawn in a random color.

Usage:
Run the script and follow the prompts:
    python turtle_painter.py

Example Output:
    (The screen will display a grid of randomly colored dots)

Instructions:
1. The turtle starts at position (-100, -100).
2. It moves in steps of 50 pixels in both the X and Y directions.
3. The turtle draws a random-colored dot each time it moves.

License:
This project is licensed under the MIT License.
"""

import turtle as t
import random


def main():
    # Set the colormode to 255 so we can use RGB values for the colors
    t.colormode(255)

    # Create a turtle (painter) and a screen for drawing
    painter = t.Turtle()
    screen = t.Screen()

    # Lift the pen so that we can move the turtle without drawing lines
    painter.penup()

    # Set initial positions and movement increments
    x = -100
    y = -100
    move_x = 50
    move_y = 50

    # Move the painter to the starting position
    painter.goto(x, y)

    # Loop to draw a grid of dots
    while painter.ycor() < abs(y) + 1 and painter.xcor() <= abs(x):
        # Generate a random color in RGB format
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        # Check if the painter is at the last column or row
        if (painter.xcor() == abs(x) and painter.ycor() < abs(y)) or (painter.xcor() == x and painter.ycor() != y):
            # Draw a dot and move the painter
            painter.dot(20, color)
            painter.setheading(90)  # Set direction to upward
            painter.forward(move_y)  # Move upward
            painter.dot(20, color)  # Draw another dot after moving

            # Change direction when reaching the end of the row or column
            if painter.xcor() == abs(x):
                painter.setheading(180)  # Turn around (left)
            else:
                painter.setheading(0)  # Turn around (right)

        # Draw a dot on the current position
        painter.dot(20, color)
        # Move the painter horizontally to the next position
        painter.forward(move_x)

    # Wait for a click on the screen to exit the program
    screen.exitonclick()


if __name__ == '__main__':
    main()