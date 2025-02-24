from cars import Cars

car1=Cars('Maruti','Red')
car2=Cars('Baleno','Green')
car3=Cars('S-Class','Black')


print(f"{car1.model} is {car1.color} in color")

print(f"{car2.model} is {car2.color} in color")

print(f"{car3.model} is {car3.color} in color")

print(f'The cars manufactured in {Cars.manufacturing_year} are {Cars.total_cars}')