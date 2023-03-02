separator = "----------------------------------------"
class Carte:
	couleurs = ["Coeur", "Carreau", "Pique", "Trèfle"]
	valeurs = ["As", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Valet", "Dame", "Roi"]

	def __init__(self, valeur, couleur):
		self.valeur = valeur
		self.couleur = couleur

class Jeu:
	def __init__(self):
		self._paquet = []
		for couleur in Carte.couleurs:
			for valeur in Carte.valeurs:
				self._paquet.append(Carte(valeur, couleur))

	def lancerJeu(self):
		jeu = True

		croupier = Joueur("Croupier")
		joueur = Joueur("Joueur1")
		self.melanger()

		self.donner(croupier) # 1ère carte du croupier
		self.donner(joueur) # 1ère carte du joueur
		self.donner(croupier) # 2ème carte du croupier
		self.donner(joueur) # 2ème carte du joueur

		while jeu:
			if croupier._score < 21 and joueur._score < 21:
				choix = input("Voulez-vous une carte? ")
				if choix == "oui":
					self.donner(joueur)
				elif choix == "non":
					if croupier._score < 17:
						self.donner(croupier)
				elif choix != "oui" or choix != "non":
					print("Veuillez répondre par oui ou non")
			elif croupier._score == joueur._score:
				print("Le jeu est terminé, égalité !")
			else:
				if croupier._score > joueur._score:
					print(f"{separator}Le jeu est terminé, le croupier est vainqueur ! {croupier._nom} a {croupier._score} points et le {joueur._nom} a {joueur._score} points")
				elif croupier._score < joueur._score:
					print(f"Le jeu est terminé, vous êtes vainqueur ! {joueur._nom} a {joueur._scorlacke} points et le {croupier._nom} a {croupier._score} points")
				jeu = False

	def melanger(self):
		import random
		random.shuffle(self._paquet)
			
	def tirer(self):
		return self._paquet.pop()
	
	def donner(self, joueur):
		carte = self.tirer()
		joueur._main.append(carte)
		joueur._score += self.valeurCarte(carte)
		print(f"{separator}\n{joueur._nom} a {carte.valeur} de {carte.couleur} \n{joueur._score} points")
	
	def valeurCarte(self, carte):
		if carte.valeur in [2, 3, 4, 5, 6, 7, 8, 9, 10]:
			return carte.valeur
		elif carte.valeur in ["Valet", "Dame", "Roi"]:
			return 10
		elif carte.valeur == "As":
			while True:
				choix = input("Voulez-vous que l'As vaille 1 ou 11? ")
				if choix == "11":
					return 11
				elif choix == "1":
					return 1
				else:
					print("Veuillez répondre par 1 ou 11")
	
class Joueur:
	def __init__(self, nom):
		self._main = []
		self._score = 0
		self._nom = nom
		
	def __str__(self):
		return f"{self._nom} a {self._score} points"

Jeu1 = Jeu()
Jeu1.lancerJeu()