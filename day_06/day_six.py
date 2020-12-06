from collections import Counter
import os
import sys


def sort_groups(raw_input_list):
    groups_list = []
    grp = []
    for i, item in enumerate(raw_input_list):
        if item == '':
            groups_list.append(grp)
            grp = []
        else:
            grp.append(item)
            if i + 1 == len(raw_input_list):
                groups_list.append(grp)
    return groups_list


if __name__ == '__main__':
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        input_list = f.read().splitlines()

    groups = sort_groups(input_list)

    flattened_groups = []
    for group in groups:
        flt_grp = {response for person in group for response in person}
        flattened_groups.append(flt_grp)

    res = sum(len(x) for x in flattened_groups)  # 1st result

    flattened_groups = []
    for group in groups:
        counter = Counter()
        for person in group:
            counter += Counter(person)
        new_group = [char for char in counter.keys() if counter[char] == len(group)]
        flattened_groups.append(new_group)

    res = sum(len(x) for x in flattened_groups)  # 2nd result
