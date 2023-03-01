class Ville :
  def __init__(self, nom, nb_habitants) :
    self.__nom = nom
    self.__nb_habitants = nb_habitants
  def __str__(self) :
    return "Ville de %s avec %d habitants" % (self.__nom, self.__nb_habitants)
  def ajouthabitant(self):
    self.__nb_habitants += 1
class Personne:
  def __init__(self, nom, age, ville):
    self.__nom = nom
    self.__age = age
    self.__ville = ville
  def __str__(self):
    return "Personne de nom %s et de ville %s" % (self.__nom, self.__prenom, self.__ville)
  def ajouthabitant(self):
    self.__ville.ajouthabitant()
  def afficherInfo(self):
    print(str(self))
    
Ville1 = Ville("Paris", 1000000)
Ville2 = Ville("Lyon", 500000)

Moi = Personne("Enzo", 20, Ville1)
livio = Personne("Livio", 25, Ville2)

print(Ville1)
print(Ville2)
Moi.ajouthabitant()
livio.ajouthabitant()
print(Ville1)
print(Ville2)
