import math
import copy

monkeys = []

with open('input.txt') as file:
	lines = file.readlines()
	count = math.ceil(len(lines) / 7)
	#print(count)

	monkeymod = 1

	for i in range(0, count):
		monkey = {'throws': 0}
		monkey['items'] = [int(x) for x in lines[i*7+1].strip().split(': ')[1].split(', ')]
		oper  = lines[i*7+2].strip().split(' ')
		monkey['is_prod']  = oper[4] == '*'
		if oper[5] != 'old':
			monkey['val'] = int(oper[5])
			monkey['val1_is_val2'] = False
		else:
			monkey['val1_is_val2'] = True
		monkey['test']  = int(lines[i*7+3].strip().split(' ')[3])
		monkey['ift']  = int(lines[i*7+4].strip().split(' ')[5])
		monkey['iff']  = int(lines[i*7+5].strip().split(' ')[5])
		monkeys.append(monkey)
		monkeymod *= monkey['test']

def get_monkey_business(monkeys_in, div_by, round_count):
	monkeys = copy.deepcopy(monkeys_in)
	for i in range(0, round_count):
		for monkey in monkeys:
			monkey['throws'] += len(monkey['items'])

			val1_is_val2 = monkey['val1_is_val2']
			if not val1_is_val2:
				val2 = monkey['val']

			is_prod = monkey['is_prod']
			test = monkey['test']
			ift = monkey['ift']
			iff = monkey['iff']

			while monkey['items']:
				# get val1
				val = monkey['items'].pop()

				# determine val2 if same as val1
				if val1_is_val2:
					val2 = val

				# apply operator
				if is_prod:
					val *= val2
				else:
					val += val2

				# integer divide
				val //= div_by

				# store only modulo of all dividers to keep value manageable
				val %= monkeymod

				# test
				if val % test == 0:
					next_monkey = ift
				else:
					next_monkey = iff

				# move to monkey
				monkeys[next_monkey]['items'].append(val)

	throws = sorted([monkey['throws'] for monkey in monkeys])

	return throws[-1] * throws[-2]

print("part 1:", get_monkey_business(monkeys, 3, 20))
print("part 2:", get_monkey_business(monkeys, 1, 10000))

