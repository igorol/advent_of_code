from itertools import groupby


def two_consecutive_digits(passwd):
    """
    return True if contains 2 consecutive equal digits
    """
    digits = str(passwd)
    groups = groupby(digits)
    results = [(label, sum(1 for _ in group)) for label, group in groups]
    results = [i[1] for i in results]
    for result in results:
        if result >= 2:
            return True
    return False


def never_decreasing_digits(passwd):
    """
    return True if, going left to right, digits never decrease
    """

    digits = list(str(passwd))

    for digit1, digit2 in zip(digits[:-1], digits[1:]):
        if digit2 < digit1:
            return False
    return True


def additional_criteria(passwd):
    """
    return True if the two adjacent matching digits 
    are not part of a larger group of matching digits
    """

    digits = str(passwd)
    groups = groupby(digits)
    results = [(label, sum(1 for _ in group)) for label, group in groups]
    results = [i[1] for i in results]
    if 2 in results:
        return True
    return False


puzzle_input = [248345, 746315]
# Part1
counter = 0
for passwd in range(puzzle_input[0], puzzle_input[1] + 1):
    if two_consecutive_digits(passwd) and never_decreasing_digits(passwd):
        counter += 1
    print(f"\r Part1 : {counter} valid passwords", end="")

print()

# Part2
counter = 0
for passwd in range(puzzle_input[0], puzzle_input[1] + 1):
    if additional_criteria(passwd) and never_decreasing_digits(passwd):
        counter += 1
    print(f"\r Part2 : {counter} valid passwords", end="")

print()

