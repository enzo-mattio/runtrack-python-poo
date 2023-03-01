'''
Créez un jeu de combat en utilisant la POO.
À tour de rôle, votre personnage et l’ennemi attaquent. Le but étant de vaincre l’ennemi
(vie à zéro).
Votre programme doit contenir au minimum deux classes, Personnage et Jeu.

Commencer par créer une classe nommée Personnage prenant des paramètres de
construction : nom (string) et vie(int).
Créez au minimum une méthode “attaquer” qui enlève des points à son adversaire.
Ensuite créer la classe “Jeu” ne prenant pas de paramètre. Créer une méthode
“choisirNiveau” qui permet de demander au joueur le niveau de difficulté. Celui-ci sera
stocké dans l’attribut niveau.
En fonction du niveau choisi, le nombre de points de vie du joueur ainsi que de l'ennemi
seront différents.
Créer “lancerJeu”, méthode qui utilise l’attribut niveau. Cette méthode aura pour but
d’instancier deux objets “Personnage”, un qui représente le joueur et l’autre l'ennemi
avec un nombre de points défini en fonction du niveau.
Implémenter le déroulement d’une partie en demandant au joueur le niveau de difficulté
et pensez à ajouter une méthode qui vérifie la santé de vos personnages ainsi qu’une
méthode permettant de vérifier qui a gagné.
'''
import random
import time
class Personnage:
  def __init__(self, nom, vie):
    self.nom = nom
    self.vie = vie

  def attaquer(self, cible):
    attque = random.randint(1, 3)
    coefattaque = random.uniform(0.8, 1.2)
    if attque == 1:
      cible.vie -= 10 * coefattaque
      print(f"\n{cible.nom} a subi", "%.2f" % (10 * coefattaque) ,"points de dégâts")
    if attque == 2:
      self.vie += 10 * coefattaque
      print(f"\n{self.nom} a gagné", "%.2f" % (10 * coefattaque) ,"points de vie")
    if attque == 3:
      cible.vie -= 20 * coefattaque
      print(f"\n{cible.nom} a subi une grosse attaque et perd", "%.2f" % (20 * coefattaque) ,"points de dégâts")
    
class Jeu:
  def __init__(self):
    self.niveau = 0

  def choisirNiveau(self):
    self.niveau = int(input("Choisissez le niveau de difficulté (1, 2 ou 3) : "))

  def lancerJeu(self):
    if self.niveau == 1:
      joueur = Personnage("Enzo", 100 * random.uniform(1, 1.5))
      ennemi = Personnage("Livio", 100 * random.uniform(1, 1.5))
    elif self.niveau == 2:
      joueur = Personnage("Enzo", 100 * random.uniform(1, 1.2))
      ennemi = Personnage("Livio", 100 * random.uniform(1, 1.2))
    elif self.niveau == 3:
      joueur = Personnage("Enzo", 100)
      ennemi = Personnage("Livio", 100)
    else:
      print("Niveau de difficulté invalide")
      return

    while joueur.vie > 0 and ennemi.vie > 0:
      joueur.attaquer(ennemi)
      time.sleep(0.5)
      ennemi.attaquer(joueur)

      print("\nVie de", joueur.nom + ":", ("%.2f" % joueur.vie), "Vie de", ennemi.nom + ":", ("%.2f" % ennemi.vie))
      time.sleep(1)
      
    if joueur.vie > 0:
      print("\n", joueur.nom, "a gagné")
    else:
      print("\n", ennemi.nom, "a gagné")
      
      
jeu = Jeu()
jeu.choisirNiveau()
jeu.lancerJeu()

