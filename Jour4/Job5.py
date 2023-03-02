class Forme:
  def aire(self):
    return 0

'''
Récupérer votre classe “Forme” crée juste au-dessus.
Créer une classe fille nommée “Cercle” qui hérite de la classe “Forme” et possédant un
attribut radius.
Surcharger la méthode “aire” dans la classe Cercle pour qu'elle renvoie l’aire du cercle.
Créez une instance de chaque classe Rectangle et Cercle et utilisez-les pour tester les
différentes surcharges de la méthode aire en affichant les résultats en console.
'''
class Cercle(Forme):
  def __init__(self, radius):
    self.radius = radius
  def __str__(self) -> str:
    return f"Le cercle de rayon {self.radius}cm, a pour aire {self.aire()}cm²"
  def aire(self):
    return 3.14 * self.radius ** 2

# Instanciation
Cercle1 = Cercle(5)
# Test Print
print(Cercle1)