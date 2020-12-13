import os
import sys
from functools import reduce


# https://fangya.medium.com/chinese-remainder-theorem-with-python-a483de81fbb8#d2da
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


if __name__ == '__main__':
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        input_list = f.read().splitlines()

    time = int(input_list[0])
    bus_times = [(int(x), int(x)-i) for i, x in enumerate(input_list[1].split(',')) if x != 'x']

    # Part 1
    departure_times = {}
    for t in bus_times:
        diff = time % t[0]
        departure_times[t[0]] = time - diff + t[0]

    bus_id = min(departure_times, key=departure_times.get)
    res = bus_id * (departure_times[bus_id] - time)
    print(res)

    # Part 2
    nums = [bus[0] for bus in bus_times]
    rems = [bus[1] for bus in bus_times]
    res = chinese_remainder(nums, rems)
    print(res)
