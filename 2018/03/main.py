import re
from collections import defaultdict

data = open("input").read().splitlines()

ids_per_points = defaultdict(set)
all_ids = set()
for claim in data:
    id_num, x, y, width, height = map(int, re.findall(r"\d+", claim))
    all_ids.add(id_num)
    for i in range(x, x + width):
        for j in range(y, y + height):
            ids_per_points[(i, j)].add(id_num)


print(f"Part 1: {sum(len(points) >1 for points in ids_per_points.values())}")

for val in ids_per_points.values():
    if len(val) > 1:
        for id_num in val:
            all_ids.discard(id_num)


print(f"Part 2: {all_ids.pop()}")
