from math import *
class circle:
    pi=22/7
    def __init__ (self,rad):
        self.rad=rad
    def area(self):
        a=circle.pi*(self.rad**2)
        print("Area of circle ",a)
    def circumference(self):
        c=2*circle.pi*self.rad
        print ("circumference of circle" , c)

r=int(input("Enter the radius: "))
p1=circle(r)
p1.area()
pi.circumference()