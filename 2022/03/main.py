import string

import pandas as pd


def common_item(a_string):
    s1, s2 = a_string[: int(len(a_string) // 2)], a_string[int(len(a_string) // 2) :]
    return list(set(s1) & set(s2))[0]


priorities = {k: v for k, v in zip(string.ascii_lowercase, range(1, 27))}
priorities.update({k: v for k, v in zip(string.ascii_uppercase, range(27, 53))})

data = pd.read_csv("input", names=["items"], header=None)
groups_of_3 = [
    data["items"][i : i + 3].to_list() for i in range(0, len(data["items"]), 3)
]

print("part 1:", data["items"].apply(common_item).map(priorities).sum())
print(
    "part 2:",
    sum(
        [priorities[list(set(s1) & set(s2) & set(s3))[0]] for s1, s2, s3 in groups_of_3]
    ),
)
