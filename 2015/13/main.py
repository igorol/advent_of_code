import re
from collections import defaultdict
from itertools import pairwise, permutations


def read_data():
    # defining `0` as the initial value of the defaultdict spares me
    # from having to add a bunch of values that I know have to be
    # equal to `0` on part 2
    result = defaultdict(lambda: 0)
    people = []
    pattern = "(.*) would (lose|gain) (\d+) happiness units by sitting next to (.*)."
    data = open("input").read().splitlines()
    for line in data:
        m = re.match(pattern, line)
        person, factor, level, other = m.groups()
        factor = 1 if factor == "gain" else -1
        level = int(level)
        result[(person, other)] = factor * level
        if person not in people:
            people.append(person)
    return result, people


def max_happiness(with_myself=False):
    scoring, people = read_data()
    if with_myself:
        people.append("myself")
    result = 0
    for arrangement in permutations(people):
        arrangement += (arrangement[0],)
        pairs = pairwise(arrangement)
        this = sum(scoring[(p[0], p[1])] + scoring[(p[1], p[0])] for p in pairs)
        result = max(result, this)
    return result


print("part 1:", max_happiness())
print("part 2:", max_happiness(with_myself=True))

# part 1: 618
# part 2: 601
