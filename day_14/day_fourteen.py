import os
import sys
import re
from collections import Counter
from itertools import product


def decimal_to_binary(n):
    return format(n, '036b')


def binary_to_decimal(n):
    return int(n, 2)


if __name__ == '__main__':
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        input_list = f.read().splitlines()

    cmd_regex = re.compile(r'.*\[([0-9]+)].*\s([0-9]+)$')

    # 1st part
    memory_add = {}
    for line in input_list:
        if line.startswith('mask'):
            mask = line.split(' = ')[1][::-1]
            zeros = [i for i, x in enumerate(mask) if x == '0']
            ones = [i for i, x in enumerate(mask) if x == '1']
        else:
            add, num = re.search(cmd_regex, line).groups()
            num = decimal_to_binary(int(num))[::-1]
            final_bin = ''
            for i, val in enumerate(num):
                if i in zeros:
                    final_bin += '0'
                elif i in ones:
                    final_bin += '1'
                else:
                    final_bin += val
            new_num = binary_to_decimal(final_bin[::-1])
            memory_add[add] = new_num
    res = sum(memory_add.values())
    print(res)

    # 2nd part
    memory_add = {}
    for line in input_list:
        if line.startswith('mask'):
            mask = line.split(' = ')[1][::-1]
            zeros = [i for i, x in enumerate(mask) if x == '0']
            ones = [i for i, x in enumerate(mask) if x == '1']
            floats = [i for i, x in enumerate(mask) if x == 'X']
        else:
            addr, num = re.search(cmd_regex, line).groups()
            add = decimal_to_binary(int(addr))[::-1]
            final_bin = ''
            for i, val in enumerate(add):
                if i in zeros:
                    final_bin += val
                elif i in ones:
                    final_bin += '1'
                elif i in floats:
                    final_bin += 'X'
                else:
                    final_bin += val
            x_count = Counter(final_bin)
            pos_comb = product([0, 1], repeat=x_count['X'])
            for tup in pos_comb:
                new_bin = final_bin[::-1]
                tup = list(tup)
                while tup:
                    new_bin = new_bin.replace('X', str(tup.pop(0)), 1)
                new_add = binary_to_decimal(new_bin)
                memory_add[new_add] = int(num)
    res = sum(memory_add.values())
    print(res)
