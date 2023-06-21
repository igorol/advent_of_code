import re
from collections import defaultdict
from random import shuffle


def read_data(part=1):
    data = open("input").read().splitlines()
    replacements = defaultdict(list)
    molecule = data[-1]
    for line in data:
        if "=>" in line:
            left, right = line.split("=>")
            if part == 1:
                replacements[left.strip()].append(right.strip())
            elif part == 2:
                replacements[right.strip()].append(left.strip())
    return replacements, molecule


def part1():
    replacements, molecule = read_data(part=1)
    variations = []
    split_molecule = re.findall("[A-Z][^A-Z]*", molecule)

    for i, atom in enumerate(split_molecule):
        if atom in replacements.keys():
            for value in replacements[atom]:
                m = split_molecule.copy()
                m[i] = value
                variations.append("".join(m))
    return len(set(variations))


def part2():
    replacements, molecule = read_data(part=2)
    steps = 0
    result = molecule
    while result != "e":
        temp_molecule = result
        keys = list(replacements.keys())
        shuffle(keys)
        for n in keys:
            if n in result:
                steps += result.count(n)
                result = result.replace(n, replacements[n][0])
        if result == temp_molecule:
            result = molecule
            steps = 0
            continue
    return steps


print("part 1:", part1())
print("part 2:", part2())

# part 1: 576
# part 2: 207
