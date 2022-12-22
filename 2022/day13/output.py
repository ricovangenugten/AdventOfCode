import json
import math
import functools

with open('input.txt') as file:
	lines = file.readlines()
	sets = math.ceil(len(lines) / 3)

	list1 = []
	list2 = []
	for i in range(0, sets):
		list1.append(json.loads(lines[i*3]))
		list2.append(json.loads(lines[i*3+1]))

right_order_count = 0

def check_lists(list1, list2):
	len1 = len(list1)
	len2 = len(list2)
	minlen = len1
	if len1 < len2:
		right_order = 1
	if len1 == len2:
		right_order = -1
	if len2 < len1:
		minlen = len2
		right_order = 0

	for i in range(0, minlen):
		item1 = list1[i]
		item2 = list2[i]
		if type(item1) is list or type(item2) is list:
			if type(item1) is not list:
				item1 = [item1]
			if type(item2) is not list:
				item2 = [item2]
			right_order_l = check_lists(item1, item2)
			if right_order_l > -1:
				return right_order_l
		elif item1 < item2:
			right_order = 1
			return right_order
		elif item1 > item2:
			right_order = 0
			return right_order

	return right_order

def check_lists_cmp(list1, list2):
	return -1 if check_lists(list1, list2) == 1 else 1


right_order_sum = 0
for i in range(len(list1)):
	#print("pair: ", i+1)
	#print(list1[i])
	#print(list2[i])
	order = check_lists(list1[i], list2[i])
	#print("right order:", order)
	if order == 1:
		right_order_sum += i+1


#print(len(list1))
print("part 1:", right_order_sum)

lists = list1 + list2 + [[2]] + [[6]]

#print(len(lists))

lists.sort(key = functools.cmp_to_key(check_lists_cmp))

for i in range(len(lists)):
	if lists[i] == [2]:
		twokey = i+1
	if lists[i] == [6]:
		sixkey = i+1

print("part 2:", twokey*sixkey)

