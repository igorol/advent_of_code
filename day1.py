import itertools
import numpy as np


def expenses(in_list, n):
    for i in itertools.combinations(in_list, n):
        if np.sum(i) == 2020:
            return np.prod(i)


test_list = [1721, 979, 366, 299, 675, 1456]

assert expenses(test_list, 2) == 514579

with open("day1.input", "r") as f:
    in_list = [int(i.rstrip()) for i in f.readlines()]

print("Part1", expenses(in_list, 2))

assert expenses(test_list, 3) == 241861950

print("Part2", expenses(in_list, 3))
