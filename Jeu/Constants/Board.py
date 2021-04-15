class Board:
	board = []
	nb_col = 6
	nb_line = 6

	def __init__(self):
		for i in range(1, self.nb_col+1):
			self.board.append(['_']*self.nb_line)

	def reset(self):
		self.board = []
		self.__init__()

	def render(self):
		for row in self.board:
			ligne = '|'
			for elem in row:
				ligne += ' ' + elem + ' |'
			print(ligne)
		ligne = '|'
		for i in range(1, self.nb_col+1):
			ligne += ' ' + str(i) + ' |'
		print(ligne)

	def isColFull(self, colonne):
		if self.board[0][colonne-1] == '_':
			return False
		return True

	def setPawn(self, couleur, colonne):
		if not self.isColFull(colonne):
			for i in reversed(range(0, self.nb_line)):
				if self.board[i][colonne-1] == '_':
					self.board[i][colonne-1] = couleur
					return

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
					while i - allignes > 0 and j + allignes < self.nb_col and self.board[i - allignes][j + allignes] == couleur:
						allignes += 1

						if allignes == objectif:
							return True

		return False

	def isBoardFull(self):
		for i in range(1, self.nb_col+1):
			if not self.isColFull(i):
				return False
		return True
