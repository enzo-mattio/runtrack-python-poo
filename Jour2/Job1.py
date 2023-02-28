class Rectangle:
  def __init__(self, longueur=0, largeur=0):
    self.__longueur = longueur
    self.__largeur = largeur
  def __str__(self):
    return "Rectangle de longueur %d et de largeur %d" % (self.__longueur, self.__largeur)
  def changerLongueur(self, longueur):
    self.__longueur = longueur
  def changerLargeur(self, largeur):
    self.__largeur = largeur
  def afficherInfo(self):
    print(str(self))
  
rect1 = Rectangle()
rect1.afficherInfo()
rect1.changerLongueur(10)
rect1.changerLargeur(5)
rect1.afficherInfo()
