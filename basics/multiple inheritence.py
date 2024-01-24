from cmath import pi
import math
class circle:
    def __init__(self,radius):
        self.radius= radius
r=int(input("Enter the radius: "))
obj=circle(r)

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
h=int(input("Enter height: "))
b=int(input("Enter base: "))
obj1=Triangle(h,b)

class area(circle,Triangle):
    def circle_area(self):
        return pi*self.radius**2
    def tri_area(self):
        return 0.5 * self.base * self.height

obj = area.circle_area(r)
obj1 = area.tri_area(h,b)
print("area=",round(obj.circle_area(),2))
print("area=",obj1.tri_area())