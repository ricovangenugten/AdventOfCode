import copy

heights = []
with open('input.txt') as file:
	for line in file.readlines():
		heights.append([int(digit) for digit in line.strip()])

# outer trees always visible
vis_trees = 2*len(heights) + 2*(len(heights[0])-2)

max_score = 0

for x in range(1, len(heights)-1):
	for y in range(1, len(heights[x])-1):
		height = heights[y][x]
		tot_vis = False
		tot_vis_score = 1

		for d in range(0, 4):
			if d == 0:
				# left
				rng = range(x-1, -1, -1)
			elif d == 1:
				# right
				rng = range(x+1, len(heights[y]))
			elif d == 2:
				# up
				rng = range(y-1, -1, -1)
			elif d == 3:
				# down
				rng = range(y+1, len(heights))

			visible = True
			vis_score = 0
			for i in rng:
				vis_score += 1
				nx = x
				ny = y
				if d < 2:
					nx = i
				else:
					ny = i

				if heights[ny][nx] >= height:
					visible = False
					break

			if visible:
				tot_vis = True

			tot_vis_score *= vis_score


		if tot_vis:
			vis_trees += 1

		if tot_vis_score > max_score:
			max_score = tot_vis_score



#print("tot:", len(heights)*len(heights[0]))
print("part 1:", vis_trees)
print("part 2:", max_score)

