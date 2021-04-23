# class Humain(Joueur):
class Humain:

	def __init__(self, color, name):
		self.color = color
		self.name = name

	def play_turn(self, board):
		nb_col = len(board.getBoard()[0])
		move_correct = False
		move = None
		while not move_correct:
			move = int(input("Où voulez-vous jouer ?"))
			if not board.isColFull(move) and 0 < move <= len(board.getBoard()[0]):
				move_correct = True
			else:
				print("Vous ne pouvez pas jouer ici.")
		return move
