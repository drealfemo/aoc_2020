import os
import re
import sys


if __name__ == '__main__':
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        input_list = f.read().splitlines()

    # 1st part
    accepted_passwords = []

    for line in input_list:
        values = line.split(' ')
        min_count = int(re.search('([0-9]+)-', values[0]).group(1))
        max_count = int(re.search('-([0-9]+)', values[0]).group(1))
        val = values[1][0]
        count = values[2].count(val)

        if min_count <= count <= max_count:
            accepted_passwords.append(values[2])

    res = len(accepted_passwords)

    # 2nd part
    accepted_passwords = []

    for line in input_list:
        values = line.split(' ')
        position_one = int(re.search('([0-9]+)-', values[0]).group(1))
        position_two = int(re.search('-([0-9]+)', values[0]).group(1))
        val = values[1][0]
        pos_in_val = [x.end() for x in re.finditer(val, values[2])]

        if len(set(pos_in_val).intersection({position_one, position_two})) == 1:
            accepted_passwords.append(values[2])

    res = len(accepted_passwords)
