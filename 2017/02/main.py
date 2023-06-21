from itertools import combinations

import pandas as pd


def part2(row):
    for pair in combinations(row, 2):
        if max(pair) % min(pair) == 0 and pair[0] != pair[1]:
            return int(max(pair) / min(pair))


data = pd.read_csv("input", sep="\t", header=None)
print(f"Part 1: {data.apply(lambda row: max(row) - min(row), axis=1).sum()}")
print(f"Part 2: {data.apply(lambda row: part2(row), axis=1).sum()}")
