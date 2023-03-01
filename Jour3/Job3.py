'''
Dans cet exercice, vous allez créer votre to do list.
Créer une classe “Tache” qui représente une tâche à faire. Cette classe a comme
attribut un titre, une description et un statut (à faire ou terminer) initialisés dans le
constructeur.
Créer une classe “ListeDeTaches” qui représentent la liste des tâches à faire ainsi que
toutes les méthodes nécessaires a la gestion de celles-ci avec comme attribut “taches”
(liste).
Ajouter les méthodes suivantes :
- “ajouterTache” qui permet d’ajouter une tache
- “supprimerTache” qui permet de supprimer une tache
- “marquerCommeFinie” qui permet de signaler que la tache est faite.
- “afficherListe” qui permet de retourner une liste de toutes les taches.
- “filterListe” qui permet de filtrer les taches par rapport à un statut et retourne
cette liste.
Tester votre code en créant plusieurs instances de “Tache”, les ajouter à la classe
“listeDeTache”, supprimer une tache, changer le statut d’une tache et afficher toutes les
taches et afficher les tâches à faire.
'''


class Tache:
	def __init__(self, titre, description, statut):
		self.titre = titre
		self.description = description
		self.statut = statut

	def affiche(self):
		print("Titre :", self.titre, "Description :",   self.description, "Statut :", self.statut)


class ListeDeTaches:
	def __init__(self):
		self.taches = []

	def ajouterTache(self, tache):
		self.taches.append(tache)

	def supprimerTache(self, tache):
		self.taches.remove(tache)

	def marquerCommeFinie(self, tache):
		self.taches.remove(tache)
		tache.statut = "Terminée"
		self.taches.append(tache)

	def afficherListe(self):
		for tache in self.taches:
			tache.affiche()

	def filterListe(self, statut):
		for tache in self.taches:
			if tache.statut == statut:
				tache.affiche()

tache1 = Tache("Faire les courses", "Acheter du pain, du lait et des oeufs", "A faire")
tache2 = Tache("Faire la vaisselle", "Laver les assiettes, les verres et les couverts", "A faire")
tache3 = Tache("Faire le ménage", "Passer l'aspirateur et balayer le sol", "Terminée")
tache4 = Tache("Faire la lessive", "Laver les vêtements", "A faire")

liste = ListeDeTaches()
liste.ajouterTache(tache1)
liste.ajouterTache(tache2)
liste.ajouterTache(tache3)
liste.ajouterTache(tache4)

liste.afficherListe()
liste.supprimerTache(tache2)
liste.marquerCommeFinie(tache1)
liste.afficherListe()
liste.filterListe("A faire")