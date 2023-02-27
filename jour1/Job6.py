class Animal:
  def __init__(self, age:int=0, prénom=None):
    self.age = age
    self.name = prénom
  def vieillir(self):
    self.age += 1
  def afficherAge(self):
    return self.age
  def afficherNom(self):
    return self.name
  def nommer(self, prénom):
    self.name = prénom

vieilAnimal = Animal()

print("Création d'un animal")
print(f"l'animal a {vieilAnimal.afficherAge()} an")
vieilAnimal.vieillir()
print(f"l'animal a {vieilAnimal.afficherAge()} ans")
vieilAnimal.nommer("Golemquirouelnamaspamousse")
print(f"l'animal s'appelle {vieilAnimal.afficherNom()}")

