heights = []
rows = 0
cols = 0

with open('input.txt', 'r') as f:
	lines = f.readlines()
	rows = len(lines)
	cols = len(lines[0])-1
	for y in range(0, rows):
		row = []
		for x in range(0, cols):
			char = lines[y][x]
			if char == 'S':
				char = 'a'
				start = (y, x)
			if char == 'E':
				end = (y, x)
				char = 'z'
			row.append(ord(char) - ord('a'))

		heights.append(row)


# determine possible neighbours for each point in nbs
def is_possible_neighbour(y, x, curval):
	if x >= 0 and x < cols and y >= 0 and y < rows:
		return heights[y][x] >= (curval-1)
	else:
		return False

nbs = []
pos_nbs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for y in range(0, rows):
	n_row = []
	for x in range(0, cols):
		n_nb = []
		for odx, ody in pos_nbs:
			oy = y + ody
			ox = x + odx
			if is_possible_neighbour(oy, ox, heights[y][x]):
				n_nb.append((oy, ox))

		n_row.append(n_nb)
	nbs.append(n_row)


def find_shortest_paths(frm, to):
	# breadth first search
	visited = [[0 for i in range(0, cols)] for i in range(0, rows)]
	visits = [to]
	solution_found = False
	first_a_found = False
	a = 0
	for i in range(0, 10000):
		next_visits = []
		for visit in visits:
			if heights[visit[0]][visit[1]] == 0 and first_a_found == False:
				first_a_found = True
				a = i
			if visit == frm:
				solution_found = True;
			elif visited[visit[0]][visit[1]] == 0:
				next_visits.extend(nbs[visit[0]][visit[1]])
				visited[visit[0]][visit[1]] = 1

		visits = next_visits

		if solution_found == True:
			break

	return (i, a)





(part1, part2) = find_shortest_paths(start, end)

print("part 1:", part1)
print("part 2:", part2)



