class cercle:
  def __init__(self,rayon):
    self.rayon = rayon
  def changerRayon(self,rayon):
    self.rayon = rayon
  def afficherinfo(self):
    return self.rayon, self.circonférence(), self.aire(), self.diamètre()
  def circonférence(self):
    return self.rayon*2*3.14
  def aire(self):
    return self.rayon**2*3.14
  def diamètre(self):
    return self.rayon*2

figure = cercle(5)
print(figure.afficherinfo())
figure.changerRayon(10)
print(figure.afficherinfo())
  