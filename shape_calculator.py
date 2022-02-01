"""
This code is related to the Budget App Chalenge. The description of the requirements are on the link bellow.
https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/polygon-area-calculator
"""


class Rectangle:
  def __init__(self, width=3, height=10):
        self.width = width
        self.height = height

  def __repr__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

  def set_width(self, width):
      self.width = width

  def set_height(self, height):
      self.height = height

  def get_area(self):
      return self.width * self.height

  def get_perimeter(self):
      return 2 * (self.width + self.height)

  def get_diagonal(self):
      return ((self.width ** 2 + self.height ** 2) ** 0.5)

  def get_picture(self):
    if self.width > 50 or self.height >50:
      return "Too big for picture."
    else:
      picture = ""
      for line in range(self.height):
        picture += ("*" * self.width) + "\n"
      return picture

  def get_amount_inside(self, other):
    if self.width >= other.width and self.height >= other.height:
      return int((self.get_area())//(other.get_area()))
    else:
      return 0
    

class Square(Rectangle):
  def __init__(self, side, height=None):    
        super().__init__()
        self.width = side
        self.height = side
  
  def __repr__(self):
    return f"Square(side={self.width})"
  
  def set_side(self, side):
      self.width = side
      self.height = side

  def set_width(self, side):
      self.set_side(side)

  def set_height(self, side):
      self.set_side(side)
