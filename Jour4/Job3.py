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
    self.longueur = longueur
    self.largeur = largeur
  def __str__(self) -> str:
    return f"Le rectangle de longueur {self.longueur}cm et de largeur {self.largeur}cm, a pour périmètre {self.perimetre()}cm et pour surface {self.surface()}cm²"
  def perimetre(self):
    return (self.longueur + self.largeur) * 2

  def surface(self):
    return self.longueur * self.largeur

  def getLongueur(self):
    return self.longueur

  def getLargeur(self):
    return self.largeur

  def setLongueur(self, longueur):
    self.longueur = longueur

  def setLargeur(self, largeur):
    self.largeur = largeur
    
class Parallelepipede(Rectangle):
  def __init__(self, longueur, largeur, hauteur):
    super().__init__(longueur, largeur)
    self.hauteur = hauteur
  
  def __str__(self) -> str:
    return f"Le parallélépipède de longueur {self.longueur}cm, de largeur {self.largeur}cm et de hauteur {self.hauteur}cm, a pour volume {self.volume()}cm³"
  
  def volume(self):
    return self.longueur * self.largeur * self.hauteur

  def getHauteur(self):
    return self.hauteur

  def setHauteur(self, hauteur):
    self.hauteur = hauteur

# Instanciation
Rectangle1 = Rectangle(5, 10)
Parallelepipede1 = Parallelepipede(5, 10, 15)

# Verification
print(Rectangle1)
print(Parallelepipede1)