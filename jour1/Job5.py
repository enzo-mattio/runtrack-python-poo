class Point:
  def __init__(self, x:int=50, y:int=50):
    self.x = x
    self.y = y
  def afficherLesPoints(self):
    return self.x, self.y
  def afficherX(self):
    return self.x
  def afficherY(self):
    return self.y
  def ChangerX(self, x):
    self.x = x
  def ChangerY(self, y):
    self.y = y

point=Point()
print(point.afficherLesPoints())
print(point.afficherX())
point.ChangerX(100)
point.ChangerY(100)
print(point.afficherLesPoints())