from string import ascii_lowercase

LETTERS = ascii_lowercase
PAIRS = [letter + letter for letter in LETTERS]
TRIPLETS = ["".join(x) for x in zip(LETTERS[:-2], LETTERS[1:-1], LETTERS[2:])]
NEXT_LETTERS = {c1: c2 for c1, c2 in zip(LETTERS, LETTERS[1:] + "a")}


def increment_password(password):
    password = [*password][::-1]
    next_pw = ""
    for i, character in enumerate(password):
        if i == 0 or password[:i] == i * ["z"]:
            next_pw += NEXT_LETTERS[character]
        else:
            next_pw += character
    return next_pw[::-1]


def is_valid(password):
    if any([p in ["i", "o", "l"] for p in password]):
        return False
    if sum([pair in password for pair in PAIRS]) < 2:
        return False
    if not any([t in password for t in TRIPLETS]):
        return False
    return True


def next_password(password):
    while True:
        password = increment_password(password)
        if is_valid(password):
            return password


puzzle_input = "hepxcrrq"
print("part 1:", p1 := next_password(puzzle_input))
print("part 2:", next_password(p1))
