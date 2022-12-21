coords = []
min_x = 500
max_x = 0
max_y = 0


with open('input.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
                coordline = [[int(num) for num in coord.split(',')] for coord in line.strip().split(' -> ')]
                for coord in coordline:
                        if coord[0] < min_x:
                                min_x = coord[0]
                        if coord[0] > max_x:
                                max_x = coord[0]
                        if coord[1] > max_y:
                                max_y = coord[1]

                coords.append(coordline)

        min_x -= 1
        max_x += 1

print(min_x, max_x)
print(max_y)

grid = [[ord('.') for i in  range(max_x-min_x)] for j in range(0, max_y)]

print(grid)
