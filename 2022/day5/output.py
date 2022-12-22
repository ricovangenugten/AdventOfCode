import copy

with open('input.txt') as file:
	lines = file.readlines()

	stacks = []
	stacks_2 = []
	for i in range(9):
		stacks.append([])
		stacks_2.append([])

	# part 1
	for line in lines:
		if line[0] == '[':
			for i in range(len(stacks)):
				entry = line[1+i*4]
				#print(entry)
				if entry != ' ':
					stacks[i].append(entry)
					stacks_2[i].append(entry)

		if len(line.strip()) == 0:
			# empty line, moves are next
			for i in range(len(stacks)):
				stacks[i].reverse()
				stacks_2[i].reverse()


		if line[0:4] == 'move':
			cmd = line.strip().split(' ')
			cmove = int(cmd[1])
			cfrom = int(cmd[3])-1
			cto = int(cmd[5])-1
			#print(cmove, cfrom, cto)

			intermediate = []
			#print(stacks_2[cfrom])
			#print(stacks_2[cto])
			for i in range(cmove):
				#part 1
				stacks[cto].append(stacks[cfrom].pop())

				# part 2
				#print(stacks_2[cfrom])
				intermediate.append(stacks_2[cfrom].pop())

			intermediate.reverse()
			#print(intermediate)
			stacks_2[cto].extend(intermediate)
			#print(stacks_2[cfrom])
			#print(stacks_2[cto])


print("part 1:")
for i in range(len(stacks)):
	print(stacks[i][-1], end="")
print()

print("part 2:")
for i in range(len(stacks_2)):
	print(stacks_2[i][-1], end="")
print()

#print(stacks_2)
