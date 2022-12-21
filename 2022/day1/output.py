with open('input.txt', 'r') as f:
	count = 0

	calories = []
	calories.append(0)

	for line in f:
		if line == "\n":
			calories.append(0)
		else:
			calories[-1] += int(line)

calories.sort()

print("part 1: %d" % calories[-1])
print("part 2: %d" % (calories[-1] + calories[-2] + calories[-3]))
