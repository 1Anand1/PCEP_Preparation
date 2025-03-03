from abc import ABC,abstractmethod

class Employee(ABC):

  def __init__(self,name,age):
    self.name=name
    self.age=age

  @abstractmethod
  def calculate_salary(self):
    pass

class Manager(Employee):
  def calculate_salary(self):
    if self.age<=30:
      print('Some error!')
    else:
      self.exp=self.age-18
      print(f"{1.5*self.exp}")

class Devloper(Employee):
  def calculate_salary(self):
   if self.age<18:
     print(' This is impossible !')
   else:
    print(f'{self.age-18}')