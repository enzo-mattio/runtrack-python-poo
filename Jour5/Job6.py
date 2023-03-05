'''
Créer un programme qui modélise un plateau de jeu, carré, de n x n cases. Placez sur ce
plateau n dames de jeu d'échecs, de manière à ce qu’aucune dame ne puisse se
“prendre”, quand cela est possible. La valeur de n'est renseignée par l’utilisateur. Quand
cela est possible, le programme devra afficher dans le terminal le plateau de jeu avec le
caractère ‘O’ pour les cases vides et le caractère ‘X’ pour représenter les dames.
'''
# Vérifie si la position actuelle est valide pour placer une dame sur le plateau
def est_valide(board, row, col, n):
  # Vérifier la colonne
  for i in range(row):
    if board[i][col] == 'X':
      return False

  # Vérifier la diagonale supérieure gauche
  i = row - 1
  j = col - 1
  while i >= 0 and j >= 0:
    if board[i][j] == 'X':
      return False
    i -= 1
    j -= 1

  # Vérifier la diagonale supérieure droite
  i = row - 1
  j = col + 1
  while i >= 0 and j < n:
    if board[i][j] == 'X':
      return False
    i -= 1
    j += 1

  # La position est valide pour placer une dame
  return True


# Fonction principale qui résout le problème N-Queens en utilisant la récursion
def placer_dames(board, row, n):
  solutions = []
    
  # Si toutes les rangées sont remplies, ajouter la solution
  if row == n:
    solutions.append([row[:] for row in board]) # ajouter une copie du plateau actuel à la liste des solutions
    return solutions
    
  # Parcourir chaque colonne de la rangée actuelle
  for col in range(n):
    if est_valide(board, row, col, n):
      # Placer une dame sur la case courante
      board[row][col] = 'X'

      # Récursivement placer des dames dans les rangées suivantes
      solutions += placer_dames(board, row + 1, n)

      # Retirer la dame de la position courante pour essayer d'autres positions
      board[row][col] = 'O'

  # Retourner toutes les solutions trouvées pour cette rangée
  return solutions


# Fonction pour afficher le plateau de jeu
def afficher_plateau(board):
  for row in board:
    print(' '.join(row)) # afficher chaque ligne du plateau


# Demander à l'utilisateur la taille du plateau de jeu
n = int(input("Entrez la taille du plateau de jeu: "))

# Créer un plateau vide de la taille demandée
board = [['O' for x in range(n)] for y in range(n)]

# Résoudre le problème N-Queens pour le plateau vide
solutions = placer_dames(board, 0, n)

# Si des solutions ont été trouvées, les afficher
if solutions:
  print("Nombre de solutions trouvées:", len(solutions))
  for i, solution in enumerate(solutions):
    print("Solution", i+1)
    afficher_plateau(solution) # afficher chaque solution
    print()
else:
  print("Aucune solution trouvée.")


