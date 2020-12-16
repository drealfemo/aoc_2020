import os
import sys

from collections import defaultdict
from math import prod
import pandas as pd


def delete_multiple_element(list_object, indices):
    indices = sorted(indices, reverse=True)
    for idx in indices:
        if idx < len(list_object):
            list_object.pop(idx)


if __name__ == '__main__':
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        input_list = f.read().splitlines()

    nearby_pos = None
    final_r = set()
    total_iv = []
    space_count = 0
    invalid_index = []
    ticket_fields = {}
    for i, line in enumerate(input_list):
        if line == '':
            space_count += 1
        elif space_count == 0:
            line = [x for x in line.split(' ')]
            field = ' '.join(line[:-3])[:-1]
            nums = [int(y) for x in line[-3::2] for y in x.split('-')]
            range_one = {x for x in range(nums[0], nums[1] + 1)}
            range_two = {x for x in range(nums[2], nums[3] + 1)}
            final_r.update(range_one.union(range_two))
            ticket_fields[field] = range_one.union(range_two)
        elif line.startswith('your'):
            ticket_pos = i + 1
        elif line.startswith('nearby'):
            nearby_pos = i + 1
        elif space_count == 2 and nearby_pos:
            t_nums = [int(x) for x in line.split(',')]
            invalid_vals = [x for x in t_nums if x not in final_r]
            if invalid_vals:
                invalid_index.append(i)
            total_iv.extend(invalid_vals)
    res = sum(total_iv)
    print(res)  # 1st result

    delete_multiple_element(input_list, invalid_index)
    df = pd.DataFrame(x.split(',') for x in input_list[nearby_pos:])
    df = df.astype(int)

    potential = defaultdict(list)
    for k, v in ticket_fields.items():
        for col in df.columns:
            if df[col].isin(v).all():
                potential[k].append(col)

    used = []
    field_pos = {}
    for k, v in sorted(potential.items(), key=lambda x: len(x[1])):
        if len(v) == 1:
            field_pos[k] = v[0]
            used.append(v[0])
        elif len(v) > 1:
            for x in v:
                if x not in used:
                    field_pos[k] = x
                    used.append(x)

    ticket = input_list[ticket_pos].split(',')
    required_field_pos = [v for k, v in field_pos.items() if k.startswith('departure')]
    res = prod(int(x) for i, x in enumerate(ticket) if i in required_field_pos)
    print(res)  # 2nd result
