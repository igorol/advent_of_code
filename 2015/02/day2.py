import itertools

import numpy as np

with open("day2.input", "r") as f:
    in_list = [[int(j) for j in i.rstrip().split("x")] for i in f.readlines()]


def calculate_paper(dims):
    dims_combs = list(itertools.combinations(dims, 2))
    dims_combs_prods = [np.prod(i) for i in dims_combs]
    area = 2 * np.sum(dims_combs_prods) + np.min(dims_combs_prods)
    return area


def calculate_ribbon(dims):
    dims.sort()
    smallest_face = dims[0:2]
    return (2 * np.sum(smallest_face)) + np.prod(dims)


assert calculate_paper([2, 3, 4]) == 58
assert calculate_paper([1, 1, 10]) == 43

print("Part1", np.sum([calculate_paper(i) for i in in_list]))

assert calculate_ribbon([2, 3, 4]) == 34
assert calculate_ribbon([1, 1, 10]) == 14

print("Part2", np.sum([calculate_ribbon(i) for i in in_list]))
