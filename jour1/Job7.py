class Personnage:
  def __init__(self, x:int=50, y:int=50):
    self.x = x
    self.y = y
  def bas(self):
    self.y += 1
  def haut(self):
    self.y -= 1
  def droite(self):
    self.x += 1
  def gauche(self):
    self.x -= 1
  def position(self):
    return self.x, self.y

coo = Personnage()

print(coo.position())
coo.bas()
coo.bas()
coo.bas()
coo.droite()
coo.droite()
coo.droite()
coo.droite()
print(coo.position())
