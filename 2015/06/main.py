import re

import numpy as np


def parse_line(line):
    input_parser = re.compile(
        r"(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)"
    )
    instruction, x1, y1, x2, y2 = re.search(input_parser, line).groups()
    return instruction, int(x1), int(y1), int(x2), int(y2)


def part1(data, grid):
    for line in data:
        instruction, x1, y1, x2, y2 = parse_line(line)
        if instruction == "turn on":
            grid[y1 : y2 + 1, x1 : x2 + 1] = True
        elif instruction == "turn off":
            grid[y1 : y2 + 1, x1 : x2 + 1] = False
        elif instruction == "toggle":
            grid[y1 : y2 + 1, x1 : x2 + 1] = np.logical_not(
                grid[y1 : y2 + 1, x1 : x2 + 1]
            )
    return np.count_nonzero(grid)


def part2(data, grid):
    for line in data:
        instruction, x1, y1, x2, y2 = parse_line(line)
        if instruction == "turn on":
            grid[y1 : y2 + 1, x1 : x2 + 1] += 1
        elif instruction == "turn off":
            grid[y1 : y2 + 1, x1 : x2 + 1] -= 1
            grid[y1 : y2 + 1, x1 : x2 + 1] = np.maximum(
                0, grid[y1 : y2 + 1, x1 : x2 + 1]
            )
        elif instruction == "toggle":
            grid[y1 : y2 + 1, x1 : x2 + 1] += 2
    return np.sum(grid)


data = open("input").read().splitlines()
print("part 1:", part1(data, np.zeros((1000, 1000), dtype=bool)))
print("part 2:", part2(data, np.zeros((1000, 1000), dtype=np.int32)))
