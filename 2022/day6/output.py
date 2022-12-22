
def find_start(data, size):
	start = 0
	for i in range(size-1, len(data)):
		is_start = True

		for j in range(size):
			for k in range(size):
				if data[i-j] == data[i-k] and j != k:
					is_start = False

		if is_start:
			start = i
			break

	return start+1



with open('input.txt') as file:
	data = file.read()

	print("part 1:", find_start(data, 4))
	print("part 2:", find_start(data, 14))


