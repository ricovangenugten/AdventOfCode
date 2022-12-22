import copy

total_space  = 70000000
needed_space = 30000000

def get_dir_size(dir):
	size = dir['local_size']
	for dir in dir['subdirs'].values():
		size += get_dir_size(dir)

	return size


with open('input.txt') as file:

	empty_dir = {'name': '', 'subdirs': {}, 'local_size': 0, 'total_size': 0}

	root_dir = copy.deepcopy(empty_dir)
	root_dir['name'] = '/'

	dirlist = []

	for line in file.readlines():
		words = line.strip().split(' ')
		if words[0] == '$':
			cmd = words[1]
			if cmd == 'cd':
				dir = words[2]
				if dir == '..':
					# handle cd to parent
					cwd = path.pop()
				elif dir == '/':
					# handle cd to root
					cwd = root_dir
					path = [cwd]
				else:
					# handle cd to dir
					path.append(cwd)
					cwd = cwd['subdirs'][dir]

		else:
			if words[0] == 'dir':
				dirname = words[1]
				newdir = copy.deepcopy(empty_dir)
				newdir['name'] = dirname
				# add to tree
				cwd['subdirs'][dirname] = newdir
				# add to list
				dirlist.append(newdir)
			else:
				cwd['local_size'] += int(words[0])


#print(dirlist)

root_size = get_dir_size(root_dir)

free_space = total_space - root_size
extra_space_needed = needed_space - free_space

#print("root:", root_size)
#print("free:", free_space)
#print("need:", extra_space_needed)

size_sum = 0
size_to_delete = root_size
for dir in dirlist:
	size = get_dir_size(dir)
	if (size <= 100000):
		size_sum += size
	if size >= extra_space_needed and size < size_to_delete:
		size_to_delete = size

print("part 1:", size_sum)
print("part 2:", size_to_delete)

