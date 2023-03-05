'''
Créer un programme demandant à l’utilisateur de renseigner un nombre entier. Votre
programme devra calculer x^n, où n est le nombre fourni par l’utilisateur, sans utiliser de
fonction autre que les vôtres. Attention, vous ne devez utiliser ni while, ni for, ni foreach
ni ... boucle. Seulement de la récursivité.
'''

def power(x, n):
  if n == 0:
    return 1
  else:
    return x * power(x, n-1)
  
print(power(int(input("Entrez un nombre entier (x): ")), int(input("Entrez un nombre entier (exposant): "))))