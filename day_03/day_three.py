from math import prod
import os
import sys


if __name__ == '__main__':
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        input_list = f.read().splitlines()

    # 1st part
    trees_found = 0
    pos = 0

    for i, line in enumerate(input_list):
        row = i + 1
        if row == 1:
            pos = 3

        if row > 1:
            new_line = line * row
            item = new_line[pos]
            if item == '#':
                trees_found += 1
            pos += 3

    # 2nd part
    pos_list = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    trees_list = []

    for num in pos_list:
        pos = 0
        trees_found = 0
        step = 2 if num[1] != 1 else 1
        for i, line in enumerate(input_list):
            row = i + 1
            if row == 1:
                pos = num[0]

            if row > 1 and step == 1:
                new_line = line * row
                item = new_line[pos]
                if item == '#':
                    trees_found += 1
                pos += num[0]

            elif row > 1 and row % 2 == 1:
                new_line = line * row
                item = new_line[pos]
                if item == '#':
                    trees_found += 1
                pos += num[0]

        trees_list.append(trees_found)

    trees_prod = prod(trees_list)  
