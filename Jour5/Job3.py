'''
Créer une fonction qui prend en paramètre une chaine de caractère. Écrire une fonction
qui permet de retourner sa longueur, sans utiliser de fonction système . Attention, vous
ne devez utiliser ni while, ni for, ni foreach
'''

def calc_len(s):
  if s == "":
    return 0
  else:
    return 1 + calc_len(s[1:])

print(calc_len(input("Entrez une chaine de caractères: ")))