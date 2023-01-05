from itertools import groupby


def look_and_say(sequence):
    groups = ["".join(group) for _, group in groupby(sequence)]
    return "".join([f"{len(group)}{min(set(group))}" for group in groups])


number = "1113122113"
for _ in range(40):
    number = look_and_say(number)
print("part 1:", len(number))

for _ in range(10):
    number = look_and_say(number)
print("part 2:", len(number))

# part 1: 360154
# part 2: 5103798
