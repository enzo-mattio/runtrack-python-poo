class Operation:
  def __init__(self,nombre1:int=0,nombre2:int=0):
    self.nombre1 = nombre1
    self.nombre2 = nombre2
  def addition(self):
    self.somme = self.nombre1 + self.nombre2
    print(f"La somme de {self.nombre1} et {self.nombre2} est {self.somme}")

op = Operation(5,6)
op.addition()


