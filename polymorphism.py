#Polymorohism

import math

class Rectangle:

    def __init__(self,tool,arz):
        self.tool = tool
        self.arz = arz
    
    def masahat(self):
        return self.tool*self.arz



class Circle:

    def __init__(self,shoa):
        self.shoa = shoa

    def masahat(self):
        return (self.shoa**2)*math.pi

class Triangle:
    
    def __init__(self,a,b,c):
        self.a =a
        self.b =b
        self.c =c
    
    def masahat(self):
        p = (self.a + self.b + self.c)//2
        return math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))



a1 = Rectangle(12,4)
a2 = Circle(4)
a3 = Triangle(6,8,10)
print(a1.masahat())
print(a2.masahat())
print(a3.masahat())