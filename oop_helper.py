import turtle
import random

class Polygon:
    def __init__(self,sides,size,orientation,location,color,border):
        # Initializes the polygon
        self.num_sides = sides
        self.size = size
        self.orientation = orientation
        self.location = location
        self.color = color
        self.border_size = border

class Drawer:
    def __init__(self):
        self.location = [0.0,0.0]

    def draw_polygon(self,polygon: Polygon, reduction_ratio=1):
        turtle.penup()
        turtle.goto(polygon.location[0], polygon.location[1])
        turtle.setheading(polygon.orientation)
        turtle.color(polygon.color)
        turtle.pensize(polygon.border_size)
        turtle.pendown()
        for _ in range(polygon.num_sides):
            turtle.forward(polygon.size * reduction_ratio)
            turtle.left(360/polygon.num_sides)
        turtle.penup()

    def get_new_color(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    def reposition(self,size,reduction_ratio):
        # reposition the turtle and get a new location
        turtle.penup()
        turtle.forward(size*(1-reduction_ratio)/2)
        turtle.left(90)
        turtle.forward(size*(1-reduction_ratio)/2)
        turtle.right(90)
        self.location = [turtle.pos()[0],turtle.pos()[1]]
