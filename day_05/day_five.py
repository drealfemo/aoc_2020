import os
import sys


def lower_half(array):
    return array[:int(len(array)/2)]


def upper_half(array):
    return array[int(len(array)/2):]


def choose_array_method(char, array):
    return {
        "F": lambda: lower_half(array),
        "B": lambda: upper_half(array),
        "L": lambda: lower_half(array),
        "R": lambda: upper_half(array),
    }.get(char, lambda: '')()


if __name__ == '__main__':
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        input_list = f.read().splitlines()

    init_rows = [x for x in range(0, 128)]
    init_columns = [x for x in range(0, 8)]

    final_seating = []

    for line in input_list:
        row_letters = line[:7]
        col_letters = line[7:]

        row = init_rows
        for val in row_letters:
            res = choose_array_method(val, row)
            row = res

        col = init_columns
        for val in col_letters:
            res = choose_array_method(val, col)
            col = res

        final_seating.append((row[0], col[0]))

    res = max([x[0] * 8 + x[1] for x in final_seating])  # 1st result

    seating_dict = {}
    for row, col in final_seating:
        seating_dict.setdefault(row, []).append(col)

    missing_row = 0
    missing_col = 0
    for row, cols in seating_dict.items():
        if set(cols) == set(init_columns):
            pass
        else:
            missing_cols = [x for x in init_columns if x not in cols]
            for m_col in missing_cols:
                if m_col + 1 in cols and m_col - 1 in cols:
                    missing_row = row
                    missing_col = m_col
                    break

    res = missing_row * 8 + missing_col  # 2nd result
