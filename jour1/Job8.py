class cercle:
  def __init__(self,rayon):
    self.rayon = rayon
  def changerRayon(self,rayon):
    self.rayon = rayon
  def afficherinfo(self):
    print(f"Rayon: {self.rayon}, Circonférence:  {self.circonférence()}, Aire: {self.aire()}, Diamètre: {self.diamètre()} \n")
  def circonférence(self):
    return self.rayon*2*3.14
  def aire(self):
    return self.rayon**2*3.14
  def diamètre(self):
    return self.rayon*2

figure = cercle(5)
figure.afficherinfo()
figure.changerRayon(10)
figure.afficherinfo()
  