# https://adventofcode.com/2022/day/2

import pandas as pd

# {<move> : [<score_rules_part1>, <score_rules_part2>]}
scores = {
    "A X": [4, 3],
    "A Y": [8, 4],
    "A Z": [3, 8],
    "B X": [1, 1],
    "B Y": [5, 5],
    "B Z": [9, 9],
    "C X": [7, 2],
    "C Y": [2, 6],
    "C Z": [6, 7],
}

data = pd.read_csv("input", header=None, names=["moves"])
sums = pd.DataFrame(data.moves.map(scores).to_list())
print("part 1: ", sums[0].sum())
print("part 2: ", sums[1].sum())
