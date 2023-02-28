class voiture:
  def __init__(self,marque, modele, annee, kilometrage:int, marche=False, reservoir=50):
    self.__marque = marque
    self.__modele = modele
    self.__annee = annee
    self.__kilometrage = kilometrage
    self.__marche = marche
    self.__reservoir = reservoir
  def __str__(self):
    return "Voiture de marque %s de modèle %s d'année %d de kilométrage %d" % (self.__marque, self.__modele, self.__annee, self.__kilometrage)
  def demarrer(self):
    if self.__marche == False and self.__verifierplein() > 5:
      self.__marche = True
      print("La voiture est démarrée")
      return True
    else:
      print("Le réservoir est vide ou la voiture est déjà démarrée")
      return False
  def arreter(self):
    if self.__marche == True:
      self.__marche = False
      print("La voiture est arrêtée")
      return True
    else:
      print("La voiture est déjà arrêtée")
      return False
  def __verifierplein(self):
    return self.__reservoir
  def changerReservoir(self, reservoir):
    self.__reservoir = reservoir
  def afficherInfo(self):
    print(str(self))
    if self.__marche == True:
      print("La voiture est démarrée")
    else:
      print("La voiture est arrêtée")
    print("Le réservoir est à %d litres" % self.__reservoir) 

voiture1 = voiture("Peugeot", "308", 2015, 10000)
voiture1.afficherInfo()
voiture1.demarrer()
voiture1.arreter()