import os
import re
import sys


def sort_passports(raw_input_list):
    passport_lists = []
    passport = []
    for i, item in enumerate(raw_input_list):
        if item == '':
            passport_lists.append(passport)
            passport = []
        else:
            passport.append(item)
            if i + 1 == len(raw_input_list):
                passport_lists.append(passport)
    return passport_lists


def convert_passport_format(passport_list):
    passport_dict = dict(data.split(':') for item in passport_list for data in item.split(' '))
    return passport_dict


def validate_passport(passport, level=1):
    """
        Level = 1 for the 1st part
        Level = 2 for the 2nd part
    """
    valid_fields = {'ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'cid', 'hgt'}
    if set(passport.keys()) == valid_fields or set(passport.keys()) == valid_fields - {'cid'}:
        if level == 2:
            valid_byr = True if len(passport['byr']) == 4 and 1920 <= int(passport['byr']) <= 2002 else False
            valid_iyr = True if len(passport['iyr']) == 4 and 2010 <= int(passport['iyr']) <= 2020 else False
            valid_eyr = True if len(passport['iyr']) == 4 and 2020 <= int(passport['eyr']) <= 2030 else False
            valid_hcl = True if re.search('^#[a-f0-9]{6}$', passport['hcl']) else False
            valid_ecl = True if re.search('^amb|blu|brn|gry|grn|hzl|oth$', passport['ecl']) else False
            valid_pid = True if re.search('^[0-9]{9}$', passport['pid']) else False

            hgt = re.search('^([0-9]{2,3})(cm|in)$', passport['hgt'])
            valid_hgt = False
            if hgt:
                if hgt.group(2) == 'cm' and 150 <= int(hgt.group(1)) <= 193:
                    valid_hgt = True
                if hgt.group(2) == 'in' and 59 <= int(hgt.group(1)) <= 76:
                    valid_hgt = True
            if valid_byr and valid_iyr and valid_eyr and valid_hcl and valid_ecl and valid_pid and valid_hgt:
                return True
        else:
            return True
    return False


if __name__ == '__main__':
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        input_list = f.read().splitlines()

    passports = sort_passports(input_list)

    p_wallet = []
    for p_port in passports:
        p_dict = convert_passport_format(p_port)
        p_wallet.append(p_dict)

    valid_passports = 0
    for p_port in p_wallet:
        is_valid_passport = validate_passport(p_port, level=2)
        if is_valid_passport:
            valid_passports += 1
