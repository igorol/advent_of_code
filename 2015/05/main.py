import re


def is_nice_p1(string):
    return (
        sum([c in "aeiou" for c in string]) >= 3
        and any([c1 == c2 for c1, c2 in zip(string[1:], string[:-1])])
        and all([x not in string for x in ["ab", "cd", "pq", "xy"]])
    )


def is_nice_p2(string):
    n1 = re.compile(r"(..).*\1")
    n2 = re.compile(r"(.).\1")
    return bool(re.search(n1, string)) and bool(re.search(n2, string))


data = open("input").read().splitlines()
print("part 1:", sum([is_nice_p1(item) for item in data]))
print("part 2:", sum([is_nice_p2(item) for item in data]))
