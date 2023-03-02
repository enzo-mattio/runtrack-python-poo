'''
Créer une classe “Rectangle” avec comme attribut privé longueur et largeur. Créer la
méthode “périmètre” permettant de calculer le périmètre du rectangle ainsi que la
méthode “surface“ permettant de calculer la surface du rectangle.
Créer les accesseurs et mutateurs permettant de manipuler les attributs de la classe.
Créer une classe “Parallélépipède“ héritant de la classe Rectangle avec en plus un
attribut hauteur et une autre méthode volume permettant de calculer le volume du
parallélépipède.
Instancier la classe Rectangle et assurez-vous que toutes les méthodes fonctionnent.
'''

class Rectangle:
  def __init__(self, longueur, largeur):
    self.__longueur = longueur
    self.__largeur = largeur
  def __str__(self) -> str:
     return f"Le rectangle de longueur {self.__longueur}cm et de largeur {self.__largeur}cm, a pour périmètre {self.perimetre()}cm et pour surface {self.surface()}cm²"
  def perimetre(self):
    return (self.__longueur + self.__largeur) * 2

  def surface(self):
    return self.__longueur * self.__largeur

  def getLongueur(self):
    return self.__longueur

  def getLargeur(self):
    return self.__largeur

  def setLongueur(self, longueur):
    self.__longueur = longueur

  def setLargeur(self, largeur):
    self.__largeur = largeur
    
class Parallelepipede(Rectangle):
  def __init__(self, longueur, largeur, hauteur):
    Rectangle.__init__(self, longueur, largeur)
    self.hauteur = hauteur
  
  def __str__(self) -> str:
    return f"Le parallélépipède de longueur {self.__longueur}cm, de largeur {self.__largeur}cm et de hauteur {self.hauteur}cm, a pour volume {self.volume()}cm³"
  
  def volume(self):
    return Rectangle.surface(self) * self.hauteur

  def getHauteur(self):
    return self.hauteur

  def setHauteur(self, hauteur):
    self.hauteur = hauteur

# Instanciation
Rectangle1 = Rectangle(5, 10)
Parallelepipede1 = Parallelepipede(5, 10, 15)

# Verification
print(Rectangle1)
print(Parallelepipede1.volume())