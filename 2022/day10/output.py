x = 1

ex_1 = [20, 60, 100, 140, 180, 220]
sum_1 = 0
vals = []

with open('input.txt', 'r') as f:
	vals.append(x)
	for line in f:
		cmd = line.strip().split(' ')

		if cmd[0] == 'addx':
			vals.append(x)
			vals.append(x)
			x += int(cmd[1])
		else:
			vals.append(x)

for i in ex_1:
	sum_1 += vals[i] * i

print("part 1:", sum_1)

print("part 2:")

for i in range(1, 241):
	if vals[i] <= i%40 <= vals[i]+2:
		print('#', end='')
	else:
		print('.', end='')

	if i % 40 == 0:
		print()






