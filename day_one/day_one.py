from itertools import combinations
from math import prod
import os
import sys


if __name__ == '__main__':
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        input_list = map(int, f.readlines())

    comb_num = 3
    res = [x for x in combinations(input_list, comb_num) if sum(x) == 2020]
    res = prod(res[0])
