from Puissance4.Jeu.Constants.Board import Board
from Puissance4.Jeu.Constants.Couleur import Couleur


class AI:
	def __init__(self, color):
		self.name = "Minimax"
		self.color = color
		self.__enemy = self.enemy_color()

	# ALGORITHME MINIMAX
	# board : pateau de jeu
	# depth : profondeur du coup testé
	# AI_turn : booléen determinant si c'est le tour de l'IA
	def thinks(self, board, depth, AI_turn):
		# Si l'IA arrive à un board correspondant à une fin de jeu ou à une profondeur de 6 coups,
		# elle arrête de chercher.
		if depth == 6 or board.winState(self.color) or board.winState(self.__enemy) or board.isBoardFull():
			return 0, self.evaluate(board)
		# Si c'est le tour de l'IA, algorithme max
		elif AI_turn:
			value = -50
			pos = -1
			for i in range(1, len(board.getBoard()[0]) + 1):
				if not board.isColFull(i):
					copyBoard = Board(self)
					copyBoard.copyBoard(board.getBoard())
					copyBoard.setPawn(self.color, i)
					v_copyboard = self.thinks(copyBoard, depth + 1, False)[1]
					if v_copyboard > value:
						value = v_copyboard
						pos = i
			return pos, value
		# Si c'est le tour de l'autre joueur, algorithme min
		else:
			value = 50
			pos = -1
			for i in range(1, len(board.getBoard()[0]) + 1):
				if not board.isColFull(i):
					copyBoard = Board(self)
					copyBoard.copyBoard(board.getBoard())
					copyBoard.setPawn(self.__enemy, i)
					v_copyboard = self.thinks(copyBoard, depth + 1, True)[1]
					if v_copyboard < value:
						value = v_copyboard
						pos = i
			return pos, value

	def evaluate(self, board):
		# 1		=> Victoire
		# 0		=> Peut importe
		# -1	=> Defaite

		if board.winState(self.color):
			return 1
		elif board.winState(self.__enemy):
			return -1
		else:
			return 0

	# choix de la couleur de l'adversaire en fonction de la couleur de l'IA
	def enemy_color(self):
		if self.color == Couleur.JAUNE:
			return Couleur.ROUGE
		else:
			return Couleur.JAUNE
