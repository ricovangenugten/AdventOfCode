def prio(char):
	decval = ord(char)

	if decval >= ord('a') and decval <= ord('z'):
		decval += 1 - ord('a')
	elif decval >= ord('A') and decval <= ord('Z'):
		decval += 27 - ord('A')
	else:
		exit('invalid char')

	return decval


sum1 = 0
sum2 = 0

with open('input.txt') as file:
	lines = file.readlines()

	# part 1
	for line in lines:
		linestr = line.strip()
		rlen = int(len(linestr) / 2)
		list1 = list(linestr[0:rlen])
		list2 = list(linestr[rlen:])
		#print(line)
		#print(list1)
		#print(list2)
		inters = set(list1).intersection(set(list2))
		#print(inters)
		if (len(inters) > 1 or len(inters) == 0):
			exit("intersection not 1")

		sum1 += prio(inters.pop())


	# part 3
	for i in range(0, len(lines), 3):
		line1 = set(list(lines[i  ].strip()))
		line2 = set(list(lines[i+1].strip()))
		line3 = set(list(lines[i+2].strip()))

		inters = line1.intersection(line2).intersection(line3)

		sum2 += prio(inters.pop())
print(sum1)
print(sum2)
