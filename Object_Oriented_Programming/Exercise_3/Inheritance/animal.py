class Animal:

  total_age=0  
  def __init__(self,name,age):
    self.name=name
    self.age=age
    Animal.total_age+=self.age


  def speaks(self):
    print(f'{self.name} says something!!!!')
    

class Dog(Animal):

  def speaks(self):
    print(f'{self.name} says WOOF!!!!')

class Cat(Animal):

  def speaks(self):
    print(f'{self.name} says MEOW!!!!')