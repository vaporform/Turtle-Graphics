# Project Overview
This project is a generative art tool using Python’s Turtle graphics. The goal is to generate geometric art compositions based on user input. The program allows the user to select from 9 different generation modes, from simple polygons to recursive shapes.

## Implementation

The original code is in procedural style, but has been rewritten into an object oriented programming (OOP) style. Every function works as intended.

# Project Structure
This repository contains the following files and directories:
- examples/
    - A directory containing example artworks from the program.

- main.py
    - The main program. It handles user input and drawing logic using the helper classes.

- oop_helper.py
    - A module containing the Polygon and Drawer classes, which handle the data structure and basic drawing commands.

- procedural.py
    - The original code written in a procedural style (for reference).

- readme.md
    - This file. Contains documentation and usage instructions.

# Design Overview
The program logic is split between main.py and oop_helper.py. The design primarily utilizes three classes: Polygon, Drawer, and App.

## Polygon (oop_helper.py)
This class acts as a data container for the geometric shapes.

- `__init__(self, sides, size, orientation, location)`
Initializes the polygon with specific attributes including the number of sides, the size (radius/length), the rotation angle, and the (x, y) coordinates.

## Drawer (oop_helper.py)
This class handles the Turtle graphics rendering and pen manipulation.

- `__init__(self)`
Initializes the drawer. Includes location, current color, and border size.

- `draw_polygon(self, polygon: Polygon, reduction_ratio=1)` Moves the turtle to the polygon's location and draws the shape based on its attributes.

- `reposition_inside(self, size, reduction_ratio)` 
Calculates a new starting position to draw a smaller shape inside a larger one.

- `random_brush(self)` Randomizes the drawing attributes, generating a new RGB color and pen thickness.

- `draw_n(self, n, polygon: Polygon, reduction_ratio)`
 A recursive method that draws `n` iterations of a polygon, shrinking it by the reduction_ratio each time to create a nested effect.

## App (main.py)
This class inherits from Drawer and manages the application loop.

- `__init__(self)` Initializes the application and superclass. Sets up configuration variables.

- `ask(self)` Handles user input with error checking. It prompts the user to select an option (1-9).

- `create_polygons(self, amount, sides)` A method that generates a list of random Polygon objects with specified constraints.

- `generate(self)` A method that generates the artwork. It checks the option selected by the user and sets up the screen. Then, it loops through the polygons to draw them.

# Running the program
Before running, ensure Python is installed on your system.
```
python3 --version
```
Next, you can download the repository directly or clone it via
```
git clone https://github.com/vaporform/Turtle-Graphics.git
```
Open the folder by using prefered IDE or in the terminal:
```
cd path/to/your/folder
```
Then, run the main program:
```
python3 main.py
```
Next, follow the on-screen prompt:
```
Which art do you want to generate? Enter a number between 1 to 9 inclusive:
```
Enter a valid number to generate the art window. To exit, simply click the 'X' on the Turtle window.