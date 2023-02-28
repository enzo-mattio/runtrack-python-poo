class Livre:
  def __init__(self, titre, auteur, nbPages,dispo=True):
    self.__titre = titre
    self.__auteur = auteur
    self.__nbPages = nbPages
    self.__dispo = dispo
  def __str__(self):
    return "Livre de titre %s de auteur %s et de contient %d Pages" % (self.__titre, self.__auteur, self.__nbPages)
  def changerTitre(self, titre):
    self.__titre = titre
  def changerAuteur(self, auteur):
    self.__auteur = auteur
  def changerNbPages(self, nbPages):
    if nbPages > 0 and nbPages==int(nbPages):
      self.__nbPages = nbPages
    else:
      print("Le nombre de pages doit être un entier positif")
  def verifierDispo(self):
    if self.__dispo == True:
      return True
    if self.__dispo == False:
      return False
  def emprunter(self):
    if self.__dispo == True:
      self.__dispo = False
      return True
    else:
      return False
  def rendre(self):
    if self.__dispo == False:
      self.__dispo = True
      return True
    else:
      return False
  def afficherInfo(self):
    print(str(self))
    if self.verifierDispo() == True:
      print("Disponibilité: Disponible")
    else:
      print("Disponibilité: Indisponible")
    
Livre1 = Livre("Le livre de la jungle", "Rudyard Kipling", 200)

Livre1.afficherInfo()
Livre1.emprunter()
Livre1.afficherInfo()
Livre1.rendre()
Livre1.afficherInfo()