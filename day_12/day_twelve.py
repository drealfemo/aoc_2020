import os
import sys


if __name__ == '__main__':
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        input_list = f.read().splitlines()

    coord = {'N': 0, 'E': 0, 'S': 0, 'W': 0}
    coord_l = list(coord) * 2
    pos = 'E'
    for line in input_list:
        action = line[0]
        value = int(line[1:])
        if action in ['N', 'E', 'S', 'W']:
            coord[action] += value
        elif action == 'F':
            coord[pos] += value
        elif action == 'L':
            degree = int(value / 90)
            n_i = coord_l.index(pos) - degree
            pos = coord_l[n_i]
        elif action == 'R':
            degree = int(value / 90)
            n_i = coord_l.index(pos) + degree
            pos = coord_l[n_i]

    vert = coord['N'] - coord['S']
    hor = coord['E'] - coord['W']
    dist = abs(vert) + abs(hor)
    print(dist)
