# Definition de la classe Personne
class Personne:
  def __init__(self, age=14):
    self.age = age

  def afficherAge(self):
    print(self.age)

  def bonjour(self):
    print('Hello')

  def modifierAge(self, age):
    self.age = age

# Creation de la classe Eleve enfant de la classe Personne
class Eleve(Personne):
  def allerEnCours(self):
    print('Je vais en cours')

  def affichageAge(self):
    print('J\'ai %d ans') % self.age

# Creation de la classe professeur enfant de la classe Personne
class professeur(Personne):
  def __init__(self, matiereEnseignee):
    self.matiereEnseignee = matiereEnseignee

  def enseigner(self):
    print('Le cours va commencer')


    
# Instanciation
p = Personne()
pierre = Eleve()
marc = professeur('Maths')


'''
À l’aide de la classe “Personne” , Eleve et Professeur écrit au-dessus, faites dire bonjour
à votre élève grâce à la méthode “bonjour” ainsi que “je vais en cours” grâce à la
méthode “allerEnCours”. Redéfinir l’age de l’élève à 15 ans.
Créer un objet Professeur, 40 ans, faite dire bonjour à votre professeur et commencer le
cours grâce à la méthode enseigner.
'''
pierre.modifierAge(15)
marc.modifierAge(40)
marc.afficherAge()
pierre.bonjour()
pierre.allerEnCours()
marc.bonjour()
marc.enseigner()
