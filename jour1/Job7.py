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
    print(f"x: {self.x}, y: {self.y}")

coo = Personnage()

coo.position()
coo.bas()
coo.bas()
coo.bas()
coo.droite()
coo.droite()
coo.droite()
coo.droite()
coo.position()
