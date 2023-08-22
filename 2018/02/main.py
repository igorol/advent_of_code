from collections import Counter

data = open("input").read().splitlines()

twos = sum(2 in c.values() for c in [Counter(box) for box in data])
threes = sum(3 in c.values() for c in [Counter(box) for box in data])

print(f"Part 1: {twos * threes}")

for box in data:
    for other_box in data:
        common_letters = "".join([c for i, c in enumerate(box) if c == other_box[i]])
        if len(common_letters) == len(box) - 1:
            print(f"Part 2: {common_letters}")
            exit()
