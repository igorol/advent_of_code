import numpy as np


def fuel_part1(mass):
    return int(np.floor(mass / 3) - 2)


def fuel_part2(mass):
    total_fuel = 0
    fuel = np.max([0, fuel_part1(mass)])
    while fuel > 0:
        total_fuel += fuel
        fuel = np.max([0, fuel_part1(fuel)])

    return int(total_fuel)


x = np.genfromtxt("day1_input.txt")

print(f"Part 1: {np.sum([fuel_part1(i) for i in x])}")
print(f"Part 2: {np.sum([fuel_part2(i) for i in x])}")
