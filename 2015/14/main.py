import re

import numpy as np


def read_data():
    pattern = r"(.*) can .* (\d+) .* (\d+) .* (\d+) .*"
    data = open("input").read().splitlines()
    info = {}
    for line in data:
        m = re.match(pattern, line).groups()
        reindeer = m[0]
        speed, last, rest = map(int, m[1:])
        info[reindeer] = {"speed": speed, "last": last, "rest": rest, "score": 0}
    return info


def fly(name, info, num_seconds):
    num_cycles = num_seconds // (info[name]["last"] + info[name]["rest"])
    rem_seconds = num_seconds % (info[name]["last"] + info[name]["rest"])
    distance = num_cycles * info[name]["last"] * info[name]["speed"]
    distance += info[name]["speed"] * min(rem_seconds, info[name]["last"])
    return distance


timestamp = 2503
reindeers = read_data()
names = list(reindeers.keys())
distances_p1 = [fly(reindeer, reindeers, timestamp) for reindeer in names]
print("part 1:", max(distances_p1))

for i in range(1, timestamp + 1):
    winner = np.argmax([fly(name, reindeers, i) for name in names])
    reindeers[names[winner]]["score"] += 1

print("part 2:", max(reindeers.values(), key=lambda x: x["score"])["score"])

# part 1: 2696
# part 2: 1084
