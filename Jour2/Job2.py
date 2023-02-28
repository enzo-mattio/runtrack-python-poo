class Livre:
  def __init__(self, titre, auteur, nbPages):
    self.__titre = titre
    self.__auteur = auteur
    self.__nbPages = nbPages
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


livbook = Livre("Le livre de la jungle", "Rudyard Kipling", 200)
print(livbook)
livbook.changerNbPages(300)
print(livbook)
livbook.changerNbPages(300.5)