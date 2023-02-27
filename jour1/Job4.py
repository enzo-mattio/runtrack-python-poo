class Person:
  def __init__(self, prénom="Louis", nom="Dupont"):
    self.prenom = prénom
    self.nom = nom
  def SePresenter(self):
    return self.prenom + " " + self.nom

op2 = Person()
print(op2.SePresenter())
op2 = Person("Jean", "Martin")
print(op2.SePresenter())