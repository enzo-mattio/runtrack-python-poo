class Etudiant:
  def __init__(self, nom, prenom, numero, points:int=0):
    self.__nom = nom
    self.__prenom = prenom
    self.__numero = numero
    self.__points = points
  def __str__(self):
    return "Etudiant de nom %s de prenom %s et de numero %d, et de niveau %s" % (self.__nom, self.__prenom, self.__numero, self.__affecterEvaluation())
  def donnerpoints(self, points):
    self.__points += points
  def __affecterEvaluation(self):
    if self.__points >= 0 and self.__points <= 60:
      return "Insuffisant"
    if self.__points >= 61 and self.__points <= 70:
      return "Passable"
    if self.__points >= 71 and self.__points <= 80:
      return "Bien"
    if self.__points >= 81 and self.__points <= 90:
      return "Très bien"
    if self.__points >= 91:
      return "Excellent"

etudiant1 = Etudiant("Moussa", "Moussa", 1)
print(etudiant1)
etudiant1.donnerpoints(50)

print(etudiant1)
etudiant1.donnerpoints(55)
print(etudiant1)