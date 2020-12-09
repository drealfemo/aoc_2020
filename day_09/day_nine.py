import os
import sys


def is_congruent_arr(array):
    for x in range(1, len(array)):
        if array[x] - array[x - 1] < 1:
            return False
    return True


if __name__ == '__main__':
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        input_list = f.read().splitlines()
    input_list = [int(x) for x in input_list]

    # 1st part
    width = 25
    step = 0
    res_one = None
    for i, num in enumerate(input_list):
        if i < width:
            continue
        preamble = input_list[step:width + step]
        for p in preamble:
            part = num - p
            if part in preamble:
                break
        else:
            res_one = num
            break
        step += 1
    print(res_one)

    # 2nd part
    valid = False
    valid_arr = []
    target = 0
    start_pos = 0
    current_pos = 0
    while not valid_arr:
        target += input_list[current_pos]
        current_pos += 1
        if target > res_one:
            target = 0
            start_pos += 1
            current_pos = start_pos
        elif target == res_one:
            sub_arr = sorted(input_list[start_pos:current_pos])
            valid = is_congruent_arr(sub_arr)
            if valid:
                valid_arr = sub_arr
    res_two = valid_arr[0] + valid_arr[-1]
    print(res_two)
