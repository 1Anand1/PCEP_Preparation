from users import Users

user1=Users('Anand',100)
user2=Users('Vivek',10)
user3=Users('Mahesh',50)
user3=Users('Vidya',40)

for each_name,each_age in zip(Users.users_list,Users.users_ages):
  print(f'{each_name} is {each_age} years old')

print(f'The total number of users are {len(Users.users_list)}')