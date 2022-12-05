import pandas as pd


def solve(row, part=1):
    pairs = [col.split("-") for col in row]
    sections = [set(range(int(pair[0]), int(pair[1]) + 1)) for pair in pairs]
    if part == 1:
        return sections[0].issubset(sections[1]) or sections[1].issubset(sections[0])
    elif part == 2:
        return bool(sections[0] & sections[1])


data = pd.read_csv("input", header=None)
print("part 1:", data.apply(solve, part=1, axis=1).sum())
print("part 2:", data.apply(solve, part=2, axis=1).sum())
