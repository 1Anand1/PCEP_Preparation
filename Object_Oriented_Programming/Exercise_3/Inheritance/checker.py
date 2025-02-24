from animal import Animal,Cat,Dog

animal_1=Animal('XYZ',20)
dog_1=Dog('Motya',25)
cat_1=Cat('Mani',26)

animal_1.speaks()
dog_1.speaks()
cat_1.speaks()

print(f'Total age is {Animal.total_age}')