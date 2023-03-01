'''Créer une classe pour représenter un joueur ainsi qu'une classe pour représenter une
équipe de foot.
La classe “Joueur” doit avoir les attributs suivants : nom, numéro, position, nombre de
buts marqués, passes décisives effectuées, cartons jaunes reçus et cartons rouges
reçus. Tous ces attributs doivent être initialisés lors de la création d'un objet Joueur.
Cette classe doit posséder les méthodes suivantes :

- “marquerUnBut”,
- “effectuerUnePasseDecisive”,
- “recevoirUnCartonJaune”,
- “recevoirUnCartonRouge”,
- “afficherStatistiques”.
Ces méthodes permettent de mettre à jour les statistiques du joueur.
La classe “Equipe” doit avoir les attributs nom et liste de joueurs. Le nom de l’équipe et
la liste de joueur (liste vide par défaut) doit être initialisé dans le constructeur.
Ajouter les méthodes suivantes :
- “ajouterJoueur”, cette méthode ajoute un joueur à l’équipe.
- “AfficherStatistiquesJoueurs”, cette méthode permet d’afficher toutes les
statistiques de l’ensemble des joueurs.
- “mettreAJourStatistiquesJoueur”, cette méthode permet de mettre à jour les
statistiques d’un joueur (buts, cartons ...).
Créer plusieurs joueurs avec les paramètres de votre choix et ajouter les aux équipes.
Présenter l’ensemble des joueurs de chaque équipe. Utiliser les différentes méthodes
afin de simuler un match, marquer un but, avoir un cation rouge... Et afficher à nouveau
les statistiques des joueurs.'''

# Classe Joueur
class Joueur:
  def __init__(self, nom, numero, position, nbButs, nbPasses, nbCartonsJaunes, nbCartonsRouges):
    self.nom = nom
    self.numero = numero
    self.position = position
    self.nbButs = nbButs
    self.nbPasses = nbPasses
    self.nbCartonsJaunes = nbCartonsJaunes
    self.nbCartonsRouges = nbCartonsRouges
  
  # Méthodes
  def marquerUnBut(self):
    self.nbButs += 1

  def effectuerUnePasseDecisive(self):
    self.nbPasses += 1

  def recevoirUnCartonJaune(self):
    self.nbCartonsJaunes += 1

  def recevoirUnCartonRouge(self):
    self.nbCartonsRouges += 1
    
  # Méthode pour afficher les statistiques d'un joueur
  def afficherStatistiques(self):
    print("\nNom :", self.nom, "\nNuméro :", self.numero, "\nPosition :", self.position, "\nNombre de buts :", self.nbButs, "\nNombre de passes :", self.nbPasses, "\nNombre de cartons jaunes :", self.nbCartonsJaunes, "\nNombre de cartons rouges :", self.nbCartonsRouges)

# Classe Equipe
class Equipe:
  def __init__(self, nom, listeJoueurs):
    self.nom = nom
    self.listeJoueurs = listeJoueurs
 
  # Méthode pour ajouter un joueur à une équipe
  def ajouterJoueur(self, joueur):
    self.listeJoueurs.append(joueur)
  
  # Méthode pour afficher les statistiques de tous les joueurs d'une équipe
  def afficherStatistiquesJoueurs(self):
    for joueur in self.listeJoueurs:
      joueur.afficherStatistiques()

  # Méthode pour mettre à jour les statistiques d'un joueur
  def mettreAJourStatistiquesJoueur(self, joueur):
    joueur.afficherStatistiques()


# Instanciation des joueurs
gronaldo = Joueur("Gronaldo", 9, "Attaquant", 0, 0, 0, 0)
messi = Joueur("Messi", 10, "Attaquant", 0, 0, 0, 0)
neymar = Joueur("Neymar", 11, "Attaquant", 0, 0, 0, 0)
mbappe = Joueur("Mbappe", 7, "Attaquant", 0, 0, 0, 0)
grosskreutz = Joueur("Grosskreutz", 8, "Milieu", 0, 0, 0, 0)
maldini = Joueur("Maldini", 3, "Défenseur", 0, 0, 0, 0)
sduarte = Joueur("Sduarte", 1, "Gardien", 0, 0, 0, 0)
eriola = Joueur("Eriola", 2, "Défenseur", 0, 0, 0, 0)


# Instanciation des équipes
psg = Equipe("PSG", [])
real = Equipe("Real Madrid", [])


# Ajout des joueurs au Real Madrid
real.ajouterJoueur(gronaldo)
real.ajouterJoueur(maldini)
real.ajouterJoueur(eriola)
real.ajouterJoueur(sduarte)
# Ajout des joueurs au PSG
psg.ajouterJoueur(messi)
psg.ajouterJoueur(neymar)
psg.ajouterJoueur(mbappe)
psg.ajouterJoueur(grosskreutz)

# Affichage des statistiques des joueurs du Real Madrid
real.afficherStatistiquesJoueurs()
# Affichage des statistiques des joueurs du PSG
psg.afficherStatistiquesJoueurs()

# Match PSG - Real Madrid
gronaldo.marquerUnBut()
maldini.effectuerUnePasseDecisive()
gronaldo.marquerUnBut()
eriola.effectuerUnePasseDecisive()
mbappe.marquerUnBut()
messi.effectuerUnePasseDecisive()
gronaldo.marquerUnBut()
eriola.effectuerUnePasseDecisive()
gronaldo.recevoirUnCartonJaune()
maldini.recevoirUnCartonRouge()

# Mis à jour des statistiques des joueurs du Real Madrid
real.mettreAJourStatistiquesJoueur(gronaldo)
real.mettreAJourStatistiquesJoueur(maldini)
real.mettreAJourStatistiquesJoueur(eriola)
# Mis à jour des statistiques des joueurs du PSG
psg.mettreAJourStatistiquesJoueur(messi)
psg.mettreAJourStatistiquesJoueur(mbappe)

# Affichage des statistiques des joueurs du Real Madrid
real.afficherStatistiquesJoueurs()
# Affichage des statistiques des joueurs du PSG
psg.afficherStatistiquesJoueurs()