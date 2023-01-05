import re
from collections import defaultdict

import numpy as np


def man_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def tuning_frequency(pos, v_max):
    return int(pos[0] * v_max + pos[1])


def get_beacon_less_x_positions(row, coords):
    pos = []
    for s_x, s_y, b_x, b_y in coords:
        remaining = man_distance((b_x, b_y), (s_x, s_y)) - abs(s_y - row)
        if remaining >= 0:
            pos.append((s_x - remaining, s_x + remaining))
    return pos


def consolidate_ranges(range_pairs):
    k, range_pairs = 0, sorted(range_pairs)
    for rng in range_pairs:
        if range_pairs[k][1] < rng[0]:
            k, range_pairs[k] = k + 1, rng
        else:
            range_pairs[k] = (range_pairs[k][0], max(range_pairs[k][1], rng[1]))
    return range_pairs[: k + 1]


def part1(coords):
    y_row = 2_000_000
    free_x = get_beacon_less_x_positions(y_row, coords)
    x_left, x_right = consolidate_ranges(free_x)[0]
    return x_right - x_left


def part2(coords):
    v_min, v_max = 0, 4_000_000
    x_limits = defaultdict(list)
    for sensor_x, sensor_y, beacon_x, beacon_y in coords:
        distance = man_distance((beacon_x, beacon_y), (sensor_x, sensor_y))
        left = np.clip(sensor_y - distance, v_min, v_max)
        right = np.clip(sensor_y + distance + 1, v_min, v_max)
        for y in range(left, right):
            dy = abs(sensor_y - y)
            x_limits[y].append((sensor_x - (distance - dy), sensor_x + (distance - dy)))

    for key, value in x_limits.items():
        val = consolidate_ranges(value)
        val = [tuple(np.clip(v, v_min, v_max)) for v in val]
        if sum(1 + x_right - x_left for x_left, x_right in val) == v_max - v_min:
            seq = np.array([])
            for v in val:
                seq = np.append(seq, np.arange(v[0], v[1] + 1))
            x = int((v_max / 2) * (v_max + 1)) - seq.sum()
            return tuning_frequency((x, key), v_max)


data = open("input").read().splitlines()
coordinates = [tuple(int(i) for i in re.findall(r"-?\d+", line)) for line in data]

print("part 1:", part1(coordinates))
print("part 2:", part2(coordinates))

# part 1: 4737443
# part 2: 11482462818989
