import os

import numpy as np


def is_passport_valid(passport_dict, strict=False):
    """return true if passport contains all required and correct fields"""

    required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    loose_verif = all(item in passport_dict.keys() for item in required)
    if strict and loose_verif:
        return strictly_verify(passport_dict)
    else:
        return loose_verif


def strictly_verify(passport_dict):

    byr = 1920 <= int(passport_dict["byr"]) <= 2002
    iyr = 2010 <= int(passport_dict["iyr"]) <= 2020
    eyr = 2020 <= int(passport_dict["eyr"]) <= 2030
    hgt = check_hgt(passport_dict["hgt"])
    hcl = check_hcl(passport_dict["hcl"])
    ecl = passport_dict["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    pid = check_pid(passport_dict["pid"])
    return byr and iyr and eyr and hgt and hcl and ecl and pid


def check_hgt(dict_item):

    int_hgt = int("".join([c for c in dict_item if c.isdigit()]))
    unit_hgt = "".join([c for c in dict_item if not c.isdigit()])
    if unit_hgt == "cm":
        hgt = 150 <= int_hgt <= 193
    elif unit_hgt == "in":
        hgt = 59 <= int_hgt <= 76
    else:
        hgt = False
    return hgt


def check_hcl(dict_item):
    item_len = len(dict_item) == 7
    hash_char = dict_item[0] == "#"
    letters = [char for char in dict_item[1:] if char.isalpha()]
    letters = all([char in "abcdef" for char in letters])
    return hash_char and item_len


def check_pid(dict_item):
    return len(dict_item) == 9 and dict_item.isnumeric()


def parse_passport(passport):
    """read string, return dict"""
    passport = passport.replace("\n", " ").split(" ")
    p = dict()
    for item in passport:
        p[item.split(":")[0]] = item.split(":")[1]
    return p


def count_valid_passports(passport_list, strict=False):
    return np.sum([is_passport_valid(p, strict=strict) for p in passport_list])


def read_input(fn):
    with open(fn) as f:
        r = f.read()
    return [parse_passport(p) for p in r.split("\n\n")]


if __name__ == "__main__":

    example_batch = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""

    example_batch = [
        parse_passport(p) for p in example_batch.split(os.linesep + os.linesep)
    ]
    assert count_valid_passports(example_batch) == 2

    passport_list = read_input("input")
    print("Part 1", count_valid_passports(passport_list))

    print("Part 2", count_valid_passports(passport_list, strict=True))
