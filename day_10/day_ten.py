import os
import sys
from collections import Counter


if __name__ == '__main__':
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        input_list = f.read().splitlines()
    input_list = sorted([int(x) for x in input_list])

    # 1st part
    diff = []
    for i, jolt in enumerate(input_list):
        if i == 0:
            diff.append(jolt - 0)
        else:
            diff.append(jolt - input_list[i - 1])

    diff.append(3)
    count = Counter(diff)
    res = count[1] * count[3]
    print(res)  # 1st result

    # 2nd part
    input_list.append(0)
    input_list = sorted(input_list)
    comb = {input_list[-1]: 1}
    print([x for x in reversed(input_list[:-1])])
    for a in reversed(input_list[:-1]):
        comb[a] = sum(comb.get(x, 0) for x in (a + 1, a + 2, a + 3))
    res = comb[0]
    print(res)  # 2nd result
