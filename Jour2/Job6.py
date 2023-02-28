class commande:
  def __init__ (self, numero):
    self.__numero = numero
    self.__liste = {}
    self.__statut = "En cours"
    self.__total = 0
  def ajouter_plat(self, nom_plat, prix):
    self.__liste[nom_plat] = {"prix": prix, "status": "en cours"}
    self.__total += prix
  def supprimerplat(self, plat):
    del self.__liste[plat]
  def __calculertotal(self):
    return self.__total
  def afficher_commande(self):
    print("Numéro de commande:", self.__numero)
    print("Plats commandés:")
    for nom_plat, details_plat in self.__liste.items():
      print("- {} ({} €) - {}".format(nom_plat, details_plat["prix"], details_plat["status"]))
    print("Total à payer HT:", self.__calculertotal(), "€")
    print("Total à payer TTC:", self.calculer_TVA(), "€")
  def calculer_TVA(self):
    return self.__total * 1.2
  
commande1 = commande(1)
commande1.ajouter_plat("Pizza", 14)
commande1.ajouter_plat("Burger", 17)
commande1.ajouter_plat("Kebab", 7)
commande1.afficher_commande()

    