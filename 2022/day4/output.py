
enclosed_count = 0
overlap_count = 0

with open('input.txt') as file:
	lines = file.readlines()

	# part 1
	for line in lines:
		pairs = line.strip().split(',')
		pair0 = [int(x) for x in pairs[0].split('-')]
		pair1 = [int(x) for x in pairs[1].split('-')]

		enclosed = False
		overlap = False

		if pair0[0] == pair1[0] or pair0[1] == pair1[1]:
			enclosed = True

		if pair0[0] > pair1[0] and pair0[1] < pair1[1]:
			enclosed = True

		if pair0[0] < pair1[0] and pair0[1] > pair1[1]:
			enclosed = True

		if enclosed:
			enclosed_count += 1

		if pair0[0] <= pair1[0] and pair0[1] >= pair1[0]:
			overlap = True

		if pair1[0] <= pair0[0] and pair1[1] >= pair0[0]:
			overlap = True

		if overlap:
			overlap_count += 1

print("part 1:", enclosed_count)
print("part 2:", overlap_count)

