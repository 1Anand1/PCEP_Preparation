class Person:
  def __init__(self,name,age):
    self.name=name
    self.age=age

class Employee(Person):
  def __init__(self,name,age,emp_id):
    super().__init__(name,age)
    self.emp_id=emp_id

class Manager(Employee):
  def __init__(self,name,age,emp_id):
    super().__init__(name,age,emp_id)

  def department(self):
    return "FEA Automation"