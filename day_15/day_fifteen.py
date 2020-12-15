import os
import sys
from collections import defaultdict


if __name__ == '__main__':
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        input_list = f.read().splitlines()
        
    values = input_list[0].split(',')
    turn_values = []
    index = defaultdict(list)
    i = 0
    while i < 30000000:  # i < 2020 for part 1 (part 2 is a bit slow - 77seconds)
        if i < len(values):
            turn_values.append(values[i])
            index[values[i]].append(i)
        else:
            last_val = turn_values[-1]
            val_index = index.get(last_val, [])
            if len(val_index) <= 1:
                turn_values.append('0')
                index['0'].append(i)
            else:
                new_val = str(val_index[-1] - val_index[-2])
                turn_values.append(new_val)
                index[new_val].append(i)
                index[new_val] = index[new_val][-2:]
        i += 1
    print(turn_values[-1])
