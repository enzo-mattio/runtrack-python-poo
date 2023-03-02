'''
Créer une classe nommée “Forme” possédant une méthode nommée aire qui renvoie 0.
Créer une classe “Rectangle” qui hérite de la classe “Forme” et qui possède deux
attributs largeur et hauteur. Surcharger la méthode aire dans la classe Rectangle afin
qu’elle ne renvoie plus 0, mais l’aire du rectangle.
Imprimer en console le résultat de la méthode aire de la classe Rectangle.
'''
class Forme:
  def aire(self):
    return 0

class Rectangle(Forme):
  def __init__(self, largeur, hauteur):
    self.largeur = largeur
    self.hauteur = hauteur
  def aire(self):
    return self.largeur * self.hauteur
  
# Instanciation
rect1 = Rectangle(5, 10)

# Print tout
print(f"L'aire du rectangle est de {rect1.aire()}cm²")