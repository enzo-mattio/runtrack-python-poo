'''
Écrire une fonction récursive permettant de retourner le plus grand chiffre d’une liste.
'''
def max_list(l):
  if len(l) == 1:
    return l[0]
  else:
    return max(l[0], max_list(l[1:]))
  
print(max_list([1, 25, 3, 4, 59, 6, 9, 8, 9, 10]))