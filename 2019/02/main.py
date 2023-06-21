import itertools

import numpy as np


def intcode(list_of_codes):
    for pointer, code in enumerate(list_of_codes):
        if pointer % 4 == 0:
            opcode = code
            if opcode == 99:
                return list_of_codes
        elif pointer % 4 == 1:
            parameter_1 = list_of_codes[code]
        elif pointer % 4 == 2:
            parameter_2 = list_of_codes[code]
        elif (pointer % 4 == 3) and (opcode == 1):
            list_of_codes[code] = parameter_1 + parameter_2
        elif (pointer % 4 == 3) and (opcode == 2):
            list_of_codes[code] = parameter_1 * parameter_2
        elif (pointer % 4 == 3) and (opcode == 99):
            return list_of_codes

    return list_of_codes


def reset_memory():
    with open("input") as f:
        lines = f.readlines()
        for line in lines:
            list_of_codes = list(np.fromstring(line, dtype=int, sep=","))
    return list_of_codes


def restore_gravity(list_of_codes):
    list_of_codes[1] = 12
    list_of_codes[2] = 2
    return list_of_codes


# Part 1
list_of_codes = reset_memory()
print(f"Part 1 : {intcode(restore_gravity(list_of_codes))[0]}")


# Part 2
def find_noun_and_verb():
    for noun, verb in list(itertools.permutations(range(100), 2)):
        list_of_codes = reset_memory()
        list_of_codes[1] = noun
        list_of_codes[2] = verb
        list_of_codes = intcode(list_of_codes)
        if list_of_codes[0] == 19690720:
            print(f"Part 2 : {100 * noun + verb}")


find_noun_and_verb()
