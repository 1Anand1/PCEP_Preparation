class Cars:

  manufacturing_year=2019
  total_cars=0

  def __init__(self,model,color):
    self.model=model
    self.color=color

    Cars.total_cars+=1