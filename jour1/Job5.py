class Point:
  def __init__(self, x:int=50, y:int=50):
    self.x = x
    self.y = y
  def afficherLesPoints(self):
    print(f"x: {self.x}, y: {self.y}")
  def afficherX(self):
    print(f"x: {self.x}")
  def afficherY(self):
    print(f"y: {self.y}")
  def ChangerX(self, x):
    self.x = x
  def ChangerY(self, y):
    self.y = y

point=Point()
point.afficherLesPoints()
point.afficherX()
point.ChangerX(100)
point.ChangerY(100)
point.afficherLesPoints()