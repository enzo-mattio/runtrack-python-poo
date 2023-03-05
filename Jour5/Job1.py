'''
Créer un programme demandant à l’utilisateur de renseigner un nombre entier. Votre
programme devra calculer la factorielle de ce nombre, sans utiliser de fonction autre
que les vôtres. Attention, vous ne devez utiliser ni while, ni for, ni foreach ni ... boucle.
Seulement de la récursivité.
'''

def fact(n):
  if n == 0:
    return 1
  else:
    return n * fact(n-1)

print(fact(int(input("Entrez un nombre entier: "))))