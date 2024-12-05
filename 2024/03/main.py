import re

input = open("input").read()

pattern = r"mul\([\d]{1,3},[\d]{1,3}\)|don't\(\)|do\(\)"
matches = re.findall(pattern, input)

matches_pt1 = [
    m.removeprefix("mul(").removesuffix(")").split(",")
    for m in matches
    if m.startswith("mul")
]
print("Part 1:", sum(int(x) * int(y) for x, y in matches_pt1))

include = True
matches_pt2 = []
for m in matches:
    if m == "don't()":
        include = False
    elif m == "do()":
        include = True
        continue
    if include:
        matches_pt2.append(m.removeprefix("mul(").removesuffix(")").split(","))
print("Part 2:", sum(int(x) * int(y) for x, y in matches_pt2))

# Part 1: 187833789
# Part 2: 94455185
