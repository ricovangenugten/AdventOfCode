def step(h_x, h_y, t_x, t_y):
	if h_x-1 <= t_x <= h_x+1 and h_y-1 <= t_y <= h_y+1:
		#print('do nothing')
		pass
	elif t_y == h_y:
		#print('move in x direction')
		if h_x > t_x:
			t_x += 1
		else:
			t_x -= 1
	elif t_x == h_x:
		#print('move in y direction')
		if h_y > t_y:
			t_y += 1
		else:
			t_y -= 1
	else:
		#print('move in diag direction')
		d_y = h_y - t_y
		d_x = h_x - t_x

		if   d_y < 0 and d_x < 0:
			t_x -= 1
			t_y -= 1
		elif d_y > 0 and d_x > 0:
			t_x += 1
			t_y += 1
		elif d_y > 0 and d_x < 0:
			t_x -= 1
			t_y += 1
		elif d_y < 0 and d_x > 0:
			t_x += 1
			t_y -= 1
		else:
			print("unexpected")

	return (t_x, t_y)

with open('input.txt', 'r') as f:
	t_x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	t_y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

	positions_1 = set()
	positions_9 = set()

	for line in f:
		cmd = line.strip().split(' ')
		dir = cmd[0]
		steps = int(cmd[1])
		#print(dir, steps)

		for i in range(0, steps):
			if dir == 'R':
				t_x[0] += 1
			if dir == 'L':
				t_x[0] -= 1
			if dir == 'U':
				t_y[0] += 1
			if dir == 'D':
				t_y[0] -= 1

			for i in range(1, 10):
				(t_x[i], t_y[i]) = step(t_x[i-1], t_y[i-1], t_x[i], t_y[i])

			#print ("H: (%d, %d), T: (%d, %d)" % (h_x, h_y, t_x, t_y))

			positions_1.add((t_x[1], t_y[1]))
			positions_9.add((t_x[9], t_y[9]))

	print("part 1:", len(positions_1))
	print("part 2:", len(positions_9))







