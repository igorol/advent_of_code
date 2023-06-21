from functools import reduce
from itertools import combinations


def solve(data, group_size=3):
    group_sum = sum(data) / group_size
    for i in range(int(len(data) / group_size)):
        quantum_entanglement = [
            reduce(lambda x, y: x * y, combination)
            for combination in combinations(data, i)
            if sum(combination) == group_sum
        ]
        if len(quantum_entanglement) > 0:
            return min(quantum_entanglement)


data = [int(i) for i in open("input").read().splitlines()]
print("part 1:", solve(data))
print("part 2:", solve(data, group_size=4))
