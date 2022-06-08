class Coordinate(object):
    def __init__(self, x ,y):
        self.x = x
        self.y = y

    def distance(self,point1):
        x_diff_sq = (self.x - point1.x)**2
        y_diff_sq = (self.y - point1.y)**2
        return (x_diff_sq + y_diff_sq)**0.5

    def __str__(self):
        return f"< {self.x}, {self.y}"

origin = Coordinate(0, 0)
point1 = Coordinate(3, 4)
print(origin.x)
print(origin.y)

print(origin.distance(point1))

print(isinstance(origin, Coordinate))
print(Coordinate.distance(origin, point1))
print(origin)
print(point1)
print(type(origin))