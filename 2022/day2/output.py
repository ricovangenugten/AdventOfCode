with open('input.txt', 'r') as f:

	op_moves = []
	my_moves = []

	op_score = {'A': 1, 'B': 2, 'C': 3}
	my_score = {'X': 1, 'Y': 2, 'Z': 3}

	game_results_1 = []
	game_results_2 = []

	for line in f:
		moves = line.strip().split(' ')
		op_move = op_score[moves[0]]
		my_move = my_score[moves[1]]

		# Part 1

		# default case: lose
		if op_move == my_move:
			# draw
			game_result_1 = 3
		elif (my_move > op_move or (my_move == 1 and op_move == 3)) and not (my_move == 3 and op_move == 1):
			# win
			game_result_1 = 6
		else:
			game_result_1 = 0

		game_results_1.append(my_move + game_result_1)

		# Part 2

		if my_move == 1:
			# need to lose
			game_result_2 = 0
			my_move_2 = op_move - 1
			if my_move_2 == 0:
				my_move_2 = 3

		elif my_move == 2:
			# need to draw
			game_result_2 = 3
			my_move_2 = op_move

		else:
			# need to win
			game_result_2 = 6
			my_move_2 = op_move + 1
			if my_move_2 == 4:
				my_move_2 = 1

		game_results_2.append(my_move_2 + game_result_2)


print("part 1: %d" % sum(game_results_1))
print("part 2: %d" % sum(game_results_2))


