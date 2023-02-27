class Person:
  def __init__(self, prénom="Louis", nom="Dupont"):
    self.prenom = prénom
    self.nom = nom
  def SePresenter(self):
    print(f"Bonjour, je suis {self.prenom} {self.nom}")

op2 = Person()
op2.SePresenter()
op2 = Person("Jean", "Martin")
op2.SePresenter()