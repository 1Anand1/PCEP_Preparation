from polymorphism import Rectangle,Circle,RectangularWaffle


waffle=RectangularWaffle(10,20)
rectangle=Rectangle(10,10.5)
circle=Circle(20)

my_shapes=[waffle,rectangle,circle]

for shape in my_shapes:
  print(f'The area is {round(shape.get_area(),1)} cm² ')