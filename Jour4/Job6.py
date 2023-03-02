'''
Créer une classe “Vehicule“ avec comme attribut une marque , une année et un prix.
Créer la méthode “informationsVehicule“ qui écrit en console la marque, le modèle,
l'année et le prix du véhicule.
Créer la classe ”Voiture“ qui hérite de la classe ”Vehicule”. Dans le constructeur de la
classe Voiture, ajouter un attribut “portes” qui contient le nombre entier 4. Créer dans
cette classe , une méthode “informationsVehicule” qui affiche, en console, les
informations générales du véhicule et le nombre de portes de la voiture.

Instancier un objet, Voiture passer les attributs dont la classe a besoin et faites appel à
la méthode “informationsVehicule”.

                    Marque : Renault
                    Modèle : Clio
Résultat attendu :  Année : 2010
                    Prix : 10000
                    Nombre de Porte : 4


Créer une classe Moto qui hérite de la classe “Vehicule” et ajouter l'attribut “roue” qui
contient par défaut l’entier 2. Créer à nouveau une méthode “informationsVehicule”
dans la classe Moto qui affiche l'intégralité des informations de la moto.
Instancier un objet Moto et faites appel à la méthode informationsVehicule.

                    Marque : Ducati
                    Modèle : Panigale 1299
Résultat attendu :  Année : 2017
                    Prix : 25000
                    Nombre de roue : 2

Créer la méthode “demarrer” dans la classe Véhicule qui écrit en console “Attention, je
roule”. Surcharger la méthode démarrer dans la classe Moto et Voiture afin d’afficher un
message personnalisé. Faites démarrer votre voiture et votre moto.
'''
separator = "========================================"
class Vehicule:
  def __init__(self, marque, modele, annee, prix):
    self.marque = marque
    self.modele = modele
    self.annee = annee
    self.prix = prix
  def demarrer(self):
    print("Attention, je roule")
  def informationsVehicule(self):
    return f"{separator} \nMarque : {self.marque}\nModèle : {self.modele}\nAnnée : {self.annee}\nPrix : {self.prix}"

class Voiture(Vehicule):
  def __init__(self, marque, modele, annee, prix, portes):
    super().__init__(marque, modele, annee, prix)
    self.portes = portes

  def informationsVehicule(self):
    return super().informationsVehicule() + f"\nNombre de Porte : {self.portes}"

class Moto(Vehicule):
  def __init__(self, marque, modele, annee, prix, roue):
    super().__init__(marque, modele, annee, prix)
    self.roue = roue
  def demarrer(self):
    print("Attention, je roule en moto, bep bep bep")
  def informationsVehicule(self):
    return super().informationsVehicule() + f"\nNombre de roue : {self.roue}"


# Instanciation
mavoiture = Voiture("Renault", "Clio", 2010, 10000, 4)
mamoto = Moto("Ducati", "Panigale 1299", 2017, 25000, 2)
# Test Print
print(mavoiture.informationsVehicule())
print(mamoto.informationsVehicule())