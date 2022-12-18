def part1(lines):
    keypad = [['1', '2', '3'],
              ['4', '5', '6'],
              ['7', '8', '9']]

    x, y = 1, 1
    password = []
    for line in lines:
        for i in line:
            x = {i == 'R': min(x + 1, 2), i == 'L': max(x - 1, 0)}.get(True, x)
            y = {i == 'D': min(y + 1, 2), i == 'U': max(y - 1, 0)}.get(True, y)
        password.append(keypad[y][x])

    return ''.join(password)


def part2(lines):
    keypad = [['0', '0', '1', '0', '0'],
              ['0', '2', '3', '4', '5'],
              ['5', '6', '7', '8', '9'],
              ['0', 'A', 'B', 'C', '0'],
              ['0', '0', 'D', '0', '0']]

    x, y = 2, 2
    password = []
    for line in lines:
        for i in line:
            left = {y == 2: 0, y in [1, 3]: 1}.get(True, 2)
            right = {y == 2: 4, y in [1, 3]: 3}.get(True, 2)
            top = {x == 2: 4, x in [1, 3]: 3}.get(True, 2)
            bottom = {x == 2: 0, x in [1, 3]: 1}.get(True, 2)
            x = {i == 'R': min(x + 1, right), i == 'L': max(x - 1, left)}.get(True, x)
            y = {i == 'D': min(y + 1, top), i == 'U': max(y - 1, bottom)}.get(True, y)
        password.append(keypad[y][x])

    return ''.join(password)


data = open('input').read().splitlines()
print('part 1:', part1(data))
print('part 2:', part2(data))
