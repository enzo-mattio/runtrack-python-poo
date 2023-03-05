'''
Écrire un programme qui demande à l’utilisateur de fournir une première chaîne de
caractères, puis une seconde. Le programme affiche 1 si les 2 chaines sont identiques
ou 0 si les chaînes ne sont pas identiques. Les chaînes ne sont constituées que de
lettres minuscules. La deuxième chaîne de caractères peut contenir un ou plusieurs ‘ * ‘.
Chaque ‘ * ‘ peut remplacer 0 ou plusieurs caractères. Par exemple, si la chaîne 1 est
“laplateforme” et la chaine 2 “lap*”, le programme affiche 1 car l’ ‘ * ‘ remplace ‘
lateforme ‘. Si la chaîne 1 est “laplateforme” et la chaîne 2 “l*a*pla*te*form***e” le
programme renvoie 1 car les ‘ * ‘ ne remplace rien.
'''

# # Première solution (fonctionne pas trop bien manque une condition pour les étoiles)
# def compare_strings(s1, s2):
# 	if s1 == s2:
# 		return 1
# 	elif s1 == "" or s2 == "":
# 		return 0
# 	elif s1[0] == s2[0]:
# 		return compare_strings(s1[1:], s2[1:])
# 	elif s2[0] == "*":
# 		return compare_strings(s1, star_replace(s1, s2))
# 	else:
# 		return "Les deux strings ne sont pas identiques"

# # Remplace les étoiles par des caractères de la chaîne de caractères
# def star_replace(s1, s2):
# 	if s2 == "":
# 		return s1
# 	elif s2[0] == "*":
# 		return star_replace(s1, s2[1:])
# 	elif s2[0] != "*":
# 		return s2[0] + star_replace(s1, s2[1:])
# 	# condition si les étoiles ne remplace rien
# 	elif s2[0] == s1[0]:
# 		return s2[0] + star_replace(s1, s2[1:])
# print(compare_strings(input("Entrez une chaine de caractères: "), input("Entrez une chaine de caractères a comparer avec la première: ")))

# Deuxième solution (fonctionne bien)

# Cette fonction prend deux chaînes de caractères en entrée et retourne True si elles sont identiques
def verifier_identique(chaine1, chaine2):
	# Vérifier si les deux chaînes sont identiques
	if chaine1 == chaine2:
		return True
	# Vérifier si les chaînes ont la même longueur et si chaque caractère correspond
	elif len(chaine1) == len(chaine2):
		for i in range(len(chaine1)):
			if chaine2[i] != '*' and chaine1[i] != chaine2[i]:
				return False
		else:
			return True
	# Si les chaînes n'ont pas la même longueur, vérifier s'il y a des '*' dans chaine2
	elif '*' in chaine2:
		# Remplacer chaque '*' par une chaîne de caractères et vérifier si le résultat correspond à chaine1
		chaine2_parts = chaine2.split('*')
		if chaine1.startswith(chaine2_parts[0]) and chaine1.endswith(chaine2_parts[-1]):
			index = len(chaine2_parts[0])
			for part in chaine2_parts[1:-1]:
				if part:
					index = chaine1.find(part, index)
					if index == -1:
						return False
					index += len(part)
				else:
					return True
		else:
			return False
	else:
			return False

# Cette fonction est une version récursive de la fonction 'verifier_identique', qui vérifie si les deux chaînes sont identiques
def verifier_identique_rec(chaine1, chaine2):
	# Cas de base : les deux chaînes sont vides ou la deuxième chaîne contient un seul '*'
	if not chaine1 and not chaine2:
		return True
	elif not chaine1 and chaine2 == '*':
		return True
	elif chaine1 and not chaine2:
		return False
	# Cas récursif : comparer le premier caractère des deux chaînes
	elif chaine2[0] != '*':
		if chaine1 and chaine1[0] == chaine2[0]:
			return verifier_identique_rec(chaine1[1:], chaine2[1:])
		else:
			return False
	else:
		# Cas récursif : '*' peut remplacer 0 ou plusieurs caractères
		for i in range(len(chaine1)+1):
			if verifier_identique(chaine1[i:], chaine2[1:]):
				return True
		else:
			return False

# Demander à l'utilisateur d'entrer les deux chaînes de caractères
chaine1 = input("Entrez la première chaîne de caractères : ")
chaine2 = input("Entrez la deuxième chaîne de caractères : ")

# Vérifier si les deux chaînes sont identiques en utilisant la version récursive de la fonction
if verifier_identique_rec(chaine1, chaine2):
	print(1)
else:
	print(0)