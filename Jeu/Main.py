from Puissance4.Jeu.Constants.AI import AI
from Puissance4.Jeu.Constants.Board import Board
from Puissance4.Jeu.Constants.Couleur import Couleur


def jouer(board):
	nb_line = board.nb_line
	nb_col = board.nb_col

	# affichage de la grille initiale
	board.render()

	# victoire = False
	compteur = 0

	while not (board.isBoardFull() or board.winState(Couleur.JAUNE) or board.winState(Couleur.ROUGE)):
		compteur += 1
		coup = None
		tour = None

		print("***** TOUR N°" + str(compteur) + " *****")

		if compteur % 2 == 1:
			tour = board.joueur1
			print(f"C'est le tour de {tour.name} : ")
			coup = tour.play_turn(board)
			# coup = tour.thinks(board, 0, True)[0]
			board.setPawn(tour.color, coup)
		elif compteur % 2 == 0:
			tour = board.joueur2
			print(f"C'est le tour de {tour.name} : ")
			# coup = tour.thinks(board, 0, True)[0]
			coup = tour.play_turn(board)

			board.setPawn(tour.color, coup)

		print(f"{tour.name} joue à la colonne {coup}")
		board.render()

	if board.winState(Couleur.JAUNE) or board.winState(Couleur.ROUGE):
		if board.winState(board.joueur1.color):
			print(f"Puissance 4, le Joueur {board.joueur1.name} a gagné!")
		elif board.winState(board.joueur2.color):
			print(f"Puissance 4, le Joueur {board.joueur2.name} a gagné!")
	else:
		print("Match nul!")


ia = AI(Couleur.JAUNE)
gameBoard = Board(ia)
jouer(gameBoard)
