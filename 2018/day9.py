import operator
import time
from utils import get_input_data, DLL

class Board(DLL):
	def move_23(self):
		return self.remove(7)

def play_game(num_players, num_marbles):
	scores = {(i+1):0 for i in range(num_players)}
	board = Board()
	turn = 1
	curr_player = 0
	while turn < num_marbles:
		if turn % 23 == 0:
			bonus = board.move_23()
			scores[curr_player+1] += bonus + turn
		else:
			board.insert(turn)
		turn += 1
		curr_player = (curr_player + 1) % num_players
	return (scores, board)

# def 

if __name__ == "__main__":
	rules = get_input_data("day9input.txt")
	split = rules[0].split(" ")
	num_players = int(split[0])
	num_marbles = int(split[-2]) + 1 # add one b/c of marble 0

	# part 1
	scores, board = play_game(num_players, num_marbles)
	k, v = max(scores.iteritems(), key=operator.itemgetter(1))
	print(k, v)

	# part 2
	start = time.time()
	large_num_marbles = int(split[-2])*100 + 1
	scores, board = play_game(num_players, large_num_marbles)
	end = time.time()
	k, v = max(scores.iteritems(), key=operator.itemgetter(1))
	print("game took %d seconds\n"%(end-start))
	print(k, v)