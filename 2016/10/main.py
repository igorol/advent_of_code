import re
from collections import defaultdict

import numpy as np


def bots_that_compare(bots_dict):
    return [i for i in bots_dict.items() if len(i[1]) == 2]


def find_targets(comparisons: list, bot_source: int):
    pattern = (
        r"bot (\d+) (gives low to) (bot|output) (\d+) (and high to) (bot|output) (\d+)"
    )
    for comparison in comparisons:
        m = re.match(pattern, comparison)
        source, target1, target2 = map(int, m.groups()[::3])
        target1_type = m.groups()[2]
        if bot_source == source:
            return target1, target1_type, target2


def solve(part2=False):
    wanted = [17, 61]
    data = open("input").read().splitlines()
    assignments = [i for i in data if i.startswith("value")]
    comparisons = [i for i in data if i.startswith("bot")]

    bots = defaultdict(list)
    outputs = defaultdict(list)
    for assignment in assignments:
        pattern = r"(value) (\d+) (goes to) (bot) (\d+)"
        m = re.match(pattern, assignment)
        bots[int(m.groups()[4])].append(int(m.groups()[1]))
        bots[int(m.groups()[4])] = sorted(bots[int(m.groups()[4])])

    while True:
        bots_to_inspect = bots_that_compare(bots)
        if wanted in bots.values() and not part2:
            return list(bots.keys())[list(bots.values()).index(wanted)]
        for bot in bots_to_inspect:
            bot_id, chips = bot[0], sorted(bot[1])
            low, low_type, high = find_targets(comparisons, bot_id)
            if low_type == "bot":
                bots[low].append(chips[0])
                bots[low] = sorted(bots[low])
            else:
                outputs[low].append(chips[0])
                outputs[low] = sorted(outputs[low])

            bots[bot_id].remove(chips[0])
            bots[bot_id] = sorted(bots[bot_id])
            bots[high].append(bots[bot_id].pop(-1))
            bots[high] = sorted(bots[high])

        if part2 and all(x in outputs.keys() for x in [0, 1, 2]):
            return np.prod([v[0] for k, v in outputs.items() if k in [0, 1, 2]])


print("part 1:", solve())
print("part 2:", solve(part2=True))

# part 1: 141
# part 2: 1209
