import os
import re
import sys


def get_bag_rules(raw_input_list):
    outer_bag = re.compile(r'^([a-z]+\s[a-z]+)\s.*')
    inner_bag = re.compile(r'([0-9]+)\s([a-z]+\s[a-z]+)\sbag')

    bags_dict = {}
    for line in raw_input_list:
        outer = re.search(outer_bag, line)
        inner = re.findall(inner_bag, line)
        bags_dict[outer.group(1)] = inner
    return bags_dict


def get_other_carriers(bags_dict, carriers):
    if not carriers:
        return []
    else:
        carriers = [k for k, v in bags_dict.items() for x in v if x[1] in carriers]
        return carriers + get_other_carriers(bags_dict, carriers)


def get_other_contents(bags_dict, contents):
    if not contents:
        return []
    else:
        c_list = []
        for content in contents:
            count = int(content[-1])
            for inner in content:
                if type(inner) != str and bags_dict[inner[1]]:
                    c_list.append(bags_dict[inner[1]] + [str(int(inner[0]) * count)])
        contents = c_list
        return contents + get_other_contents(bags_dict, contents)


if __name__ == '__main__':
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        input_list = f.read().splitlines()

    bags_order = get_bag_rules(input_list)

    direct_carriers = [k for k, v in bags_order.items() for x in v if x[1] == 'shiny gold']
    indirect_carriers = set(get_other_carriers(bags_order, direct_carriers))
    direct_carriers = set(direct_carriers)
    res_one = len(direct_carriers.union(indirect_carriers))  # 1st result

    direct_contents = bags_order['shiny gold'] + ['1']
    indirect_contents = get_other_contents(bags_order, [direct_contents])
    total_contents = [direct_contents] + indirect_contents

    res_two = 0  # 2nd result is the final value
    for data in total_contents:
        bag_count = int(data[-1])
        inners = sum(int(x[0]) for x in data if type(x) != str)
        res_two += bag_count * inners
