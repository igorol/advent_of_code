import numpy as np
import pandas as pd

df = pd.read_table("input", header=None, sep="\s+")

left_list = np.sort(df.iloc[:, 0].values)
right_list = np.sort(df.iloc[:, 1].values)

part_1 = np.abs(left_list - right_list).sum()

print("Part 1:", part_1)

unique, counts = np.unique(right_list, return_counts=True)
unique_counts = dict(zip(list(unique), list(counts)))

part_2 = 0
for val in left_list:
    try:
        part_2 += val * unique_counts[val]
    except KeyError:
        pass

print("Part 2:", part_2)
