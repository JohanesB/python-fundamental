from math import pi, sqrt
class Line():

    def __init__(self, coor1, coor2) -> None:
        self.cordinator1 = coor1
        self.cordinator2 = coor2
    
    def distance(self):
        print (sqrt((self.cordinator2[1] - self.cordinator1[1]) **2  + (self.cordinator2[0] - self.cordinator1[0]) **2))

    def slope(self):
        slop = (self.cordinator2[1] - self.cordinator1[1]) / (self.cordinator2[0] - self.cordinator1[0])
        print(slop)

    def __str__(self) -> str:
        return (f"{self.cordinator1[0]}")

coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)
print(li.distance())
print(li.slope())


class Cylinder():
    def __init__(self, height = 1, radius = 1) -> None:
        self.height = height
        self.radius = radius

    def volume(self):   # PI * r **2 * h
        volume = pi * self.radius ** 2 * self.height
        print(volume)
    def surface_area(self):  # 2 * pi * r * h + 2 * pi * r**2
        area = (2 * pi * self.radius * self.height) + 2 * pi * self.radius **2
        print(area)

c = Cylinder(2, 3)
print(c.volume())
print(c.surface_area())
