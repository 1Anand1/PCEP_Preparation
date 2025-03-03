from abc import ABC,abstractmethod
import math

class Shape(ABC):

  @abstractmethod
  def get_area(self):
    pass

class Circle(Shape):
  def __init__(self,radius):
    self.radius=radius
  
  def get_area(self):
    return math.pi*(self.radius**2)
  
class Rectangle(Shape):
  def __init__(self,base,height):
    self.base=base
    self.height=height

  def get_area(self):
    return self.base*self.height
  
class RectangularWaffle(Rectangle):
  def __init__(self, base, height):
    super().__init__(base, height)
    
  def get_area(self):
    return super().get_area()