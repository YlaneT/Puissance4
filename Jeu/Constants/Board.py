from Puissance4.Jeu.Constants.Couleur import Couleur
from Puissance4.Jeu.Constants.Humain import Humain


class Board:

	def __init__(self, ia):
		self.board = []
		self.nb_col = 7
		self.nb_line = 6
		self.joueur1 = Humain(Couleur.ROUGE, "J1")
		self.joueur2 = Humain(Couleur.JAUNE, "J2")
		# self.joueur2 = ia

		for i in range(1, self.nb_line + 1):
			line = []

			for j in range(1, self.nb_col + 1):
				line.append("_")

			self.board.append(line)

	"""
	Deep copy du tableau de jeu pour les tests de l'IA
	@param board : plateau de jeu à copier
	:return: deepCopy
	"""
	def copyBoard(self, board):
		for i in range(self.nb_col):
			for j in range(self.nb_line):
				self.board[j][i] = board[j][i]

	""" Reinitialise le plateau de jeu """
	def reset(self, ia):
		self.board = []
		self.__init__(ia)

	def getColorValue(self, value):
		if value == Couleur.ROUGE:
			return "R"
		elif value == Couleur.JAUNE:
			return "J"
		else:
			return "_"

	""" Affiche le board """
	def render(self):
		for row in self.board:
			ligne = '|'
			for elem in row:
				ligne += ' ' + self.getColorValue(elem) + ' |'
			print(ligne)
		ligne = '|'
		for i in range(1, self.nb_col + 1):
			ligne += ' ' + str(i) + ' |'
		print(ligne)

	""" Retourne True si la colonne en paramètre est pleine """
	def isColFull(self, colonne):
		if self.board[0][colonne - 1] == '_':
			return False
		return True

	""" Place un pion en prenant la gravité en compte """
	def setPawn(self, couleur, colonne):
		if not self.isColFull(colonne):
			for i in reversed(range(0, self.nb_line)):
				if self.board[i][colonne - 1] == '_':
					self.board[i][colonne - 1] = couleur
					return

	"""
	Détermine si le joueur dont la couleur est entrée en paramètre gagne la partie
	return booleen
	"""
	def winState(self, couleur):
		objectif = 4
		for i in range(0, self.nb_line):
			for j in range(0, self.nb_col):
				if self.board[i][j] == couleur:
					# checker la ligne
					allignes = 1

					while j + allignes < self.nb_col and self.board[i][j + allignes] == couleur:
						allignes += 1

						if allignes == objectif:
							return True

					# checker la colonne
					allignes = 1
					while i + allignes < self.nb_line and self.board[i + allignes][j] == couleur:
						allignes += 1

						if allignes == objectif:
							return True

					# checker la diagonale basse
					allignes = 1

					while i + allignes < self.nb_line and j + allignes < self.nb_col and self.board[i + allignes][
						j + allignes] == couleur:
						allignes += 1

						if allignes == objectif:
							return True

					# checker la diagonale haute
					while i - allignes > 0 and j + allignes < self.nb_col and self.board[i - allignes][
						j + allignes] == couleur:
						allignes += 1

						if allignes == objectif:
							return True
		return False

	# Renvoie True si le plateau de jeu est plein
	def isBoardFull(self):
		for i in range(1, self.nb_col + 1):
			if not self.isColFull(i):
				return False
		return True

	# Renvoie le plateau de jeu
	def getBoard(self):
		return self.board
