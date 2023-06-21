from collections import Counter

import pandas as pd


def valid_passphrase(row):
    words = row.values[0].split()
    return len(words) == len(set(words))


def has_anagram(row):
    counts = [Counter(word) for word in row.values[0].split()]
    for count in counts:
        if counts.count(count) > 1:
            return True
    return False


data = pd.read_csv("input", header=None)

print(f"Part 1: {data.apply(valid_passphrase, axis=1).sum()}")
print(
    f"Part 2: {data.apply(lambda row: valid_passphrase(row) and not has_anagram(row), axis=1).sum()}"
)

# Part 1: 337
# Part 2: 231
