class Produit:
  def __init__(self, nom, prixHT, TVA=1.2):
    self.nom = nom
    self.prixHT = prixHT
    self.TVA = TVA
  def afficherProduit(self):
    print(f"Produit: {self.nom}, PrixHT: {self.prixHT}, PrixTTC: {self.CalculerPrixTTC()}") 
  def afficherPrixTTC(self):
    print(f"Prix TTC: {self.CalculerPrixTTC()}")
  def afficherNom(self):
    print(f"Nom du produit: {self.nom}")
  def afficherPrixHT(self):
    print(f"{self.prixHT}")
  def changerproduit(self, nom, prixHT):
    self.nom = nom
    self.prixHT = prixHT   
  def CalculerPrixTTC(self):
    return ("%.2f" % (self.prixHT * self.TVA))
  
produit1 = Produit("PS5", 499.99)

produit1.afficherProduit()
produit1.changerproduit("GPU", 799.99)
produit1.afficherProduit()
produit1.afficherNom()
print(f"le prix TTC est de {produit1.CalculerPrixTTC()}")
