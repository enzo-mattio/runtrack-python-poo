class Operation:
  def __init__(self,nombre1:int=0,nombre2:int=0):
    self.nombre1 = nombre1
    self.nombre2 = nombre2
  def addition(self):
    return self.nombre1 + self.nombre2

op = Operation(5,6)
addition = op.addition()
print("L'addition de ", op.nombre1, " et ", op.nombre2, " est: ", addition)
