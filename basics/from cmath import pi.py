from math import *
class details(object):
    def _init_(self,radius):
        self.radius=radius
class details2(object):
    def _init_(self, height, base):
        self.height = height
        self.base = base
class area(details):
    def _init_(self,radius,height,base):
        details._init_(self,radius)
        details2._init_(self,height,base)
    def areac(self):
        return pi*self.radius*self.radius
    def areat(self):
        return 0.5*self.height*self.base
a=float(input("enter radius:"))
b=float(input("enter height:"))
c=float(input("enter base:"))
obj1=area(a,b,c)
print("area of circle:", obj1.areac())
print("area of triangle:",obj1.areat())