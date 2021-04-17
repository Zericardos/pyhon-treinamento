# Python Object Oriented Programming by Joe Marini course example
# Using Abstract Base Classes to implement interfaces

from abc import ABC, abstractmethod

#create  another class to avoid needless replication
class JSONify(ABC):
    @abstractmethod
    def toJSON(self):
        pass
    
class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass

"""
This will cause an error because abstractmethod require the implement
of function loaded must be overrided, but toJSON wasn't called

class Circle(GraphicShape, JSONify):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius ** 2)
"""
class Circle(GraphicShape, JSONify):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius ** 2)
    
    def toJSON(self):
        return f"{{\" Circle\" : {str(self.calcArea())}}}"
    
c = Circle(10)
print(c.calcArea())
