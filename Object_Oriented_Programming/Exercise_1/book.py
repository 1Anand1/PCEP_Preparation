class Book:
  # Defining the constructor
  def __init__(self,author:str,pages:int,name:str):
    self.author=author
    self.pages=pages
    self.name=name

  # Creating a describe method for describing the book
  def describe(self):
    print(f"{self.name} is written by {self.author} & it has {self.pages} pages")