class	Mammal:
  def warm_blooded(self):
    return True
  
class Bird:
  def can_fly(self):
    return "Can Fly !!"

class Bat(Mammal,Bird):
  def can_fly(self):
    return "Bats Can Fly !!"