from itertools import cycle

import numpy as np
from scipy.spatial import distance


def spiral(end):
    moves = [
        lambda x, y: (x + 1, y),  # right
        lambda x, y: (x, y - 1),  # down
        lambda x, y: (x - 1, y),  # left
        lambda x, y: (x, y + 1),
    ]  # up
    _moves = cycle(moves)
    n = 1
    pos = 0, 0
    number_of_moves = 1

    yield n, pos

    while True:
        for _ in range(2):
            move = next(_moves)
            for _ in range(number_of_moves):
                if n >= end:
                    return
                pos = move(*pos)
                n += 1
                yield n, pos

        number_of_moves += 1


def part1(end):
    return sum(list(spiral(end))[-1][1])


def part2(end):
    new_spiral = [(1, (0, 0))]
    for n, pos in spiral(end):
        if n > 1:
            x = sum(
                a for a, b in new_spiral if distance.euclidean(pos, b) <= np.sqrt(2)
            )
            new_spiral.append((x, pos))
            if x > end:
                return x


N = 265149
print(f"Part 1 : {part1(N)}")
print(f"Part 2 : {part2(N)}")

# Part 1 : 438
# Part 2 : 266330
