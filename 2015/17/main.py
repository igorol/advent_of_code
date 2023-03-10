from itertools import combinations

sizes = [int(size) for size in open("input").read().splitlines()]

configs = []
for i in range(1, len(sizes) + 1):
    configs += [config for config in combinations(sizes, i) if sum(config) == 150]

print('part 1:', len(configs))
print('part 2:', len([c for c in configs if len(c) == min([len(x) for x in configs])]))

# part 1: 654
# part 2: 57
