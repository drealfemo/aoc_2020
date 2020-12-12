import os
import sys
from collections import Counter
from itertools import chain


if __name__ == '__main__':
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        input_list = f.read().splitlines()
    input_list = [list(x) for x in input_list]
    print(input_list)

    container = [input_list]
    while True:
        curr_list = container[-1]
        out = []
        for i, row in enumerate(curr_list):
            out_r = []
            for j, seat in enumerate(row):
                if seat != ".":
                    left = "-" if j == 0 else curr_list[i][j-1]
                    right = "-" if j == len(row) - 1 else curr_list[i][j+1]
                    up = "-" if i == 0 else curr_list[i - 1][j]
                    down = "-" if i == len(curr_list) - 1 else curr_list[i+1][j]
                    up_left = "-" if i == 0 or j == 0 else curr_list[i-1][j-1]
                    up_right = "-" if i == 0 or j == len(row) - 1 else curr_list[i-1][j+1]
                    down_left = "-" if i == len(curr_list) - 1 or j == 0 else curr_list[i+1][j-1]
                    down_right = "-" if i == len(curr_list) - 1 or j == len(row) - 1 else curr_list[i+1][j+1]
                    seats_around = Counter(
                        [left, right, up, down, up_left, up_right, down_left,
                         down_right]
                    )
                    if seat == "L" and seats_around["#"] == 0:
                        out_r.append('#')
                    elif seat == "#" and seats_around["#"] >= 4:
                        out_r.append('L')
                    else:
                        out_r.append(seat)
                else:
                    out_r.append(seat)

            out.append(out_r)
        container.append(out)
        if len(container) >= 2:
            if container[-1] == container[-2]:
                break
    print(container[-1])
    final_seating = chain.from_iterable(container[-1])
    f_s = Counter(''.join(f) for f in final_seating)
    res = f_s["#"]
    print(res)
