class Animal:
  def __init__(self, age:int=0, prénom=None):
    self.age = age
    self.name = prénom
  def vieillir(self):
    self.age += 1
  def afficherAge(self):
    print(f"l'animal a {self.age} ans")
  def afficherNom(self):
    print(f"l'animal s'appelle {self.name}")
  def nommer(self, prénom):
    self.name = prénom

vieilAnimal = Animal()

print("Création d'un animal")
vieilAnimal.afficherAge()
vieilAnimal.vieillir()
vieilAnimal.afficherAge()
vieilAnimal.nommer("Golemquirouelnamaspamousse")
vieilAnimal.afficherNom()

