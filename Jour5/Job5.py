'''
Écrire une fonction récursive qui calcule le n-ième nombre de la suite de Fibonacci.
La suite de Fibonacci est une suite de nombres où chaque nombre est la somme des
deux nombres précédents. Elle commence par 0 et 1, et les premiers termes sont donc :
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, etc.
Attention, vous ne devez utiliser ni while, ni for, ni foreach,ni ... boucle. Seulement de la
récursivité.
'''
# Cette fonction prend un nombre entier n en entrée et renvoie le nombre de Fibonacci correspondant à la fin de la séquence.
def end_of_fibonacci(n):
  if n == 0: # Si n est 0, alors le nombre de Fibonacci est 0
    return 0
  elif n == 1: # Si n est 1, alors le nombre de Fibonacci est 1
    return 1
  else:
    return end_of_fibonacci(n-1) + end_of_fibonacci(n-2) # Si n est supérieur à 1, le nombre de Fibonacci est la somme des deux nombres de Fibonacci précédents
  
# Appel de la fonction et affichage du résultat pour n = 25
print(end_of_fibonacci(25)) # Résultat : 75025