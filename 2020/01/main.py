import itertools

import numpy as np


def expenses(in_list, n):
    arr = np.array(list(itertools.combinations(in_list, n)))
    mask = arr.sum(axis=1) == 2020
    return np.prod(arr[mask])


if __name__ == "__main__":
    test_list = [1721, 979, 366, 299, 675, 1456]

    assert expenses(test_list, 2) == 514579

    with open("input", "r") as f:
        in_list = [int(i.rstrip()) for i in f.readlines()]

    print("Part1", expenses(in_list, 2))

    assert expenses(test_list, 3) == 241861950

    print("Part2", expenses(in_list, 3))
