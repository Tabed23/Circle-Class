import math

class Point:
    x = 0
    y = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @property
    def Point(self):
        return self.x, self.y

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def get_y(self):
        return self.y


    def distance(self, Point):
        nx = self.x - Point.x
        ny = self.y - Point.y
        return nx, ny



class Circle:

    radius = 0.0
    p = Point()

    def __init__(self, r, y, x):
        self.radius = r
        self.p.set_x(x)
        self.p.set_y(y)

    def area(self):
        return math.pi * math.pow(self.radius, 2)

    def set_radius(self, r):
        self.radius = r

    def get_radius(self):
        return self.radius
