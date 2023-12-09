from math import prod

data = open("input").read().splitlines()
digits = ".1234567890"
part_numbers = []
gears = []
nx, ny = len(data[0]), len(data)

# part 1 : checking for part numbers
for y, line in enumerate(data):
    x = 0
    while x < nx:
        number_lenght = 0
        if data[y][x].isnumeric():
            while x < nx and data[y][x].isnumeric():
                number_lenght += 1
                x += 1
            number = int(line[x - number_lenght : x])
            if any(
                chr not in digits
                for lin in range(max(0, y - 1), min(ny, y + 2))
                for chr in data[lin][max(0, x - number_lenght - 1) : min(nx, x + 1)]
            ):
                part_numbers.append(number)
        else:
            x += 1

# part 2 : checking for gears


def get_numbers(line, x):
    start = end = x
    while start >= 0 and line[start].isnumeric():
        start -= 1
    while end < len(line) and line[end].isnumeric():
        end += 1
    return int(line[start + 1 : end])


gear_rations = []
for y, line in enumerate(data):
    for x, c in enumerate(line):
        if c == "*":
            s = set(
                get_numbers(data[yy], xx)
                for yy in range(max(0, y - 1), min(len(data) + 1, y + 2))
                for xx in range(max(0, x - 1), min(len(line) + 1, x + 2))
                if data[yy][xx].isdigit()
            )
            if len(s) == 2:
                gear_rations.append(prod(s))


print("Part 1:", sum(part_numbers))
print("Part 2:", sum(gear_rations))

# Part 1: 529618
# Part 2: 77509019
