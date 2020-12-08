import os
import re
import sys
from copy import deepcopy


if __name__ == '__main__':
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        input_list = f.read().splitlines()

    cmd_regex = re.compile(r'^([a-z]{3})\s([+|-][0-9]+)\s?([0-9]+,.?)*?$')

    # 1st part
    accumulator = 0
    pos = 0
    for i, line in enumerate(input_list):
        if i == 0:
            line = input_list[i]
        else:
            line = input_list[pos]
        cmd = re.search(cmd_regex, line).group(1)
        num_op = int(re.search(cmd_regex, line).group(2))
        cmd_history = re.search(cmd_regex, line).group(3)
        if cmd == 'nop':
            if i != 0:
                input_list[pos] = input_list[pos] + ' ' + str(i + 1) + ','
                pos += 1
            else:
                input_list[i] = input_list[i] + ' ' + str(i+1) + ','
                pos += 1
            if cmd_history:
                break
        elif cmd == 'acc':
            if i != 0:
                input_list[pos] = input_list[pos] + ' ' + str(i + 1) + ','
                pos += 1
            else:
                input_list[i] = input_list[i] + ' ' + str(i+1) + ','
                pos += 1
            if cmd_history:
                break
            accumulator += num_op
        elif cmd == 'jmp':
            if i != 0:
                input_list[pos] = input_list[pos] + ' ' + str(i + 1) + ','
                pos += num_op
            else:
                input_list[i] = input_list[i] + ' ' + str(i+1) + ','
                pos = num_op + i
            if cmd_history:
                break
    res = accumulator  # 1st result

    # 2nd part
    original_list = input_list
    for i in range(len(original_list)):
        i_list = deepcopy(original_list)
        accumulator = 0
        pos = 0
        num_tries = 0

        ln = i_list[i]
        cm = re.search(cmd_regex, ln).group(1)
        if cm == 'jmp':
            i_list[i] = i_list[i].replace('jmp', 'nop')
        elif cm == 'nop':
            i_list[i] = i_list[i].replace('nop', 'jmp')
        else:
            continue
        while 0 <= pos < len(i_list) and num_tries < 300:  # num_tries was selected randomly
            line = i_list[pos]
            cmd = re.search(cmd_regex, line).group(1)
            num_op = int(re.search(cmd_regex, line).group(2))
            if cmd == 'nop':
                pos += 1
            elif cmd == 'acc':
                pos += 1
                accumulator += num_op
            elif cmd == 'jmp':
                pos += num_op
            num_tries += 1
        if pos == len(i_list):
            res = accumulator  # 2nd result
