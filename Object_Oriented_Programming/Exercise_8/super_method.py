class Employee:
  def __init__(self,name,age):
    self.name=name
    self.age=age

  def get_details(self):
    print(f'{self.name} is the employee of a company')

class Manager(Employee):
  def __init__(self, name, age,department):
    super().__init__(name, age)
    self.department=department
  
  def get_details(self):
    super().get_details()
    print(f'This employee manages {self.department} department')

class Developer(Employee):
  def __init__(self, name, age,language):
    super().__init__(name, age)
    self.language=language

  def get_details(self):
    super().get_details()
    print(f'This developer can code in {self.language}')