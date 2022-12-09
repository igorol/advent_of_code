import numpy as np


def part1(fn):
    with open(fn) as f:
        r = f.read()
    return np.sum([len(set(p.replace("\n", ""))) for p in r.split("\n\n")])


def part2(fn):
    with open(fn) as f:
        raw = f.read()

    answers = [answer.split("\n") for answer in raw.split("\n\n")]

    count = 0

    for answer in answers:
        for i, item in enumerate(answer):
            if i == 0:
                r = set(item)
            else:
                r = r.intersection(set(item))
        count += len(r)

    return count


if __name__ == "__main__":

    print("Part1", part1("day6.input"))
    print("Part2", part2("day6.input"))
