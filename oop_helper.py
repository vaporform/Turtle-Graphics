import turtle
import random

class Polygon:
    def __init__(self,sides,size,orientation,location):
        # Initializes the polygon
        self.num_sides = sides
        self.size = size
        self.orientation = orientation
        self.location = location

class Drawer:
    def __init__(self):
        self.location = [0.0,0.0]
        self.color = None
        self.border_size = None

    def draw_polygon(self,polygon: Polygon, reduction_ratio=1):
        turtle.penup()
        turtle.goto(polygon.location[0], polygon.location[1])
        turtle.setheading(polygon.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(polygon.num_sides):
            turtle.forward(polygon.size * reduction_ratio)
            turtle.left(360/polygon.num_sides)
        turtle.penup()

    def get_new_color(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    def reposition_inside(self,size,reduction_ratio):
        # reposition the turtle into a polygon and get a new location
        turtle.penup()
        turtle.forward(size*(1-reduction_ratio)/2)
        turtle.left(90)
        turtle.forward(size*(1-reduction_ratio)/2)
        turtle.right(90)
        self.location = [turtle.pos()[0],turtle.pos()[1]]

    def random_brush(self):
        self.color = self.get_new_color()
        self.border_size = random.randint(1, 10)
    
    def draw_n(self,n, polygon: Polygon, reduction_ratio):
        for i in range(n):
            self.draw_polygon(polygon, reduction_ratio**i)
            self.reposition_inside(polygon.size,reduction_ratio)
            polygon.location = self.location
            polygon.size = polygon.size * (reduction_ratio**i)
