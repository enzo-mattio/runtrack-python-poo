class CompteBancaire:
  def __init__(self, nom, prenom, solde, numero):
    self.__nom = nom
    self.__prenom = prenom
    self.__solde = solde
    self.__numero = numero
    self.__decouvert = self.decouvert()

  def versement(self, somme):
    if self.decouvert():
      self.agios()
    if somme < self.__solde:
      self.__solde += somme
    else:
      print("Vous n'avez pas assez d'argent sur votre compte pour effectuer ce versement.")

  def retrait(self, somme):
    if self.decouvert():
      self.agios()
    if somme < self.__solde:
      self.__solde -= somme
      print("Le retrait de", somme, "euros a été effectué avec succès. Nouveau solde :", self.__solde, "euros.")

    else:
      print("Vous n'avez pas assez d'argent sur votre compte pour effectuer ce retrait.")
  def virement(self, somme, compte):
    if self.decouvert():
      self.agios()
    if somme < self.__solde:
      self.__solde -= somme
      compte.__solde += somme
      print("Le virement de", somme, "euros a été effectué avec succès. Nouveau solde :", self.__solde, "euros.")
    else:
      print("Vous n'avez pas assez d'argent sur votre compte pour effectuer ce virement.")
  def decouvert(self):
    if self.__solde < 0:
      return True
    else:
      return False
  def agios(self):
    if self.decouvert():
      self.__solde -= 10
  def affiche(self):
    if self.decouvert():
      self.agios()
      print("Le solde du compte bancaire de", self.__nom, "est de", self.__solde, "euros. Vous êtes à découvert.")
    else:
      print("Le solde du compte bancaire de", self.__nom, "est de", self.__solde, "euros.")

compte1 = CompteBancaire("Dupont", "Jean", 1000, 123456789)
compte2 = CompteBancaire("Durand", "Marie", -100, 987654321)

compte1.affiche()
compte2.affiche()
compte1.virement(500, compte2)
compte1.affiche()
compte2.affiche()


