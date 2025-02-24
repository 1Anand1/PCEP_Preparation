class Users:
  users_list=[]
  users_ages=[]
  def __init__(self,name,age):
    self.name=name
    self.age=age
    Users.users_list.append(self.name)
    Users.users_ages.append(self.age)
    