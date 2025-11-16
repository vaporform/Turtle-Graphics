from oop_helper import *

class App(Drawer):
    def __init__(self, ):
        # Initialize the app, canvas, and turtle.
        super(App,self).__init__()
        # Create some stuff...
        self.option = None
        self.amount = None
        self.reduction_ratio = None

    def ask(self):
        # Ask the user.
        while True:
            op = input("Which art do you want to generate? Enter a number between 1 to 9 inclusive: ")
            try:
                op = int(op)
                if 1 <= op <= 9:
                    self.option = op
                    break
                raise 
            except:
                print("Invalid choice! Try again.")
        
    def show_canvas(self):
        # Finish and show the results.
        turtle.done()

    def rand(self,a,b):
        # Return some random variable from a to b.
        return random.randint(a,b)
    
    def create_polygons(self,amount,sides):
        polygons = []
        for _ in range(amount):
            size = random.randint(50, 150)
            orientation = random.randint(0, 90)
            location = [random.randint(-300, 300), random.randint(-200, 200)]
            polygons.append(Polygon(sides,size,orientation,location))  
        return polygons
    
    def generate(self):
        option = self.option
        # Configs!
        # NORMALS: 1 2 3 [4]
        # DOUBLES: 5 6 7 [8]
        # MIX: 9
        # Triangle:1,5, Rectangle:2,6, Hexagon:3,7
        # 4,8,9 are all of shapes.

        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        turtle.colormode(255)
        
        self.amount = self.rand(10,20)
        # Grab some polys.

        if option in (1,4,9):
            for i in self.create_polygons(self.amount,3):
                self.random_brush()
                self.draw_polygon(i)
        if option in (2,4,9):
            for i in self.create_polygons(self.amount,4):
                self.random_brush()
                self.draw_polygon(i)
        if option in (3,4,9):
            for i in self.create_polygons(self.amount,5):
                self.random_brush()
                self.draw_polygon(i)
        
        if option in (5,8,9):
            for i in self.create_polygons(self.amount,3):
                self.random_brush()
                self.draw_n(3,i,0.618)
        if option in (6,8,9):
            for i in self.create_polygons(self.amount,4):
                self.random_brush()
                self.draw_n(3,i,0.618)
        if option in (7,8,9):
            for i in self.create_polygons(self.amount,5):
                self.random_brush()
                self.draw_n(3,i,0.618)
        
        
        # hold the window; close it by clicking the window close 'x' mark
        turtle.done()

# RUN THE PROGRAM!
Win = App()
Win.ask()
Win.generate()
