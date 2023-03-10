import numpy as np
from functools import reduce, lru_cache
from collections import defaultdict


@lru_cache()
def divisors(n):
    step = 2 if n % 2 else 1
    return sorted(set(reduce(list.__add__, ([i, n // i] for i in range(1, int(np.sqrt(n)) + 1, step) if n % i == 0))))


def part1(puzzle_input):
    house_number = 1
    while True:
        presents = np.sum(divisors(house_number)) * 10
        if presents >= puzzle_input:
            return house_number
        house_number += 1


def part2(puzzle_input):
    houses_per_elf = defaultdict(int)
    house_number = 1
    while True:
        presents = 0
        for elf in divisors(house_number):
            if houses_per_elf[elf] < 50:
                houses_per_elf[elf] += 1
                presents += elf * 11
        if presents >= puzzle_input:
            return house_number
        house_number += 1


inp = 34_000_000
print('part 1:', part1(inp))
print('part 2:', part2(inp))

# part 1: 786240
# part 2: 831600
