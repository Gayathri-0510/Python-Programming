from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        print("Area of a rectangle : ",self.length*self.breadth)
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print("Area of a circle : ",3.14*self.radius*self.radius)

rec=Rectangle(10,5)
cir=Circle(5)
rec.area()
cir.area()