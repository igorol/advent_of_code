def evaluate(line):
    winning, you_have = line.split(":")[1].split("|")
    return set(winning.split()).intersection(set(you_have.split()))


data = open("input").read().splitlines()
part1 = 0
part2 = [1] * len(data)
for idx, line in enumerate(data):
    if matching := evaluate(line):
        part1 += 2 ** (len(matching) - 1)
        for other_idx in range(1, len(matching) + 1):
            part2[idx + other_idx] += part2[idx]

print("Part 1:", part1)
print("Part 2:", sum(part2))

# Part1:  23847
# Part2:  8570000
