data = [line.strip() for line in open("input").readlines()]
num_rows = len(data)
num_columns = len(data[0])

directions = [
    (0, 1),  # right
    (1, 0),  # down
    (1, 1),  # right down
    (1, -1),  # left down
    (0, -1),  # left
    (-1, 0),  # up
    (-1, -1),  # left up
    (-1, 1),  # right up
]


def check_part1(x, y, dx, dy):
    word = "XMAS"
    word_length = len(word)
    for i in range(word_length):
        nx, ny = x + i * dx, y + i * dy
        try:
            if (
                nx < 0
                or ny < 0
                or nx >= num_rows
                or ny >= num_columns
                or data[nx][ny] != word[i]
            ):
                return 0
        except:
            pass
    return 1


def check_part2(x, y):
    if data[x][y] == "A" and 0 < x < num_rows - 1 and 0 < y < num_columns - 1:
        if (
            # M . S
            #   A
            # M . S
            (data[x - 1][y - 1] == "M" and data[x + 1][y + 1] == "S")
            and (data[x - 1][y + 1] == "M" and data[x + 1][y - 1] == "S")
            # S . M
            #   A
            # S . M
            or (data[x - 1][y - 1] == "S" and data[x + 1][y + 1] == "M")
            and (data[x - 1][y + 1] == "S" and data[x + 1][y - 1] == "M")
            # S . S
            #   A
            # M . M
            or (data[x - 1][y - 1] == "S" and data[x + 1][y + 1] == "M")
            and (data[x - 1][y + 1] == "M" and data[x + 1][y - 1] == "S")
            # M . M
            #   A
            # S . S
            or (data[x - 1][y - 1] == "M" and data[x + 1][y + 1] == "S")
            and (data[x - 1][y + 1] == "S" and data[x + 1][y - 1] == "M")
        ):
            return 1
    return 0


part1 = 0
part2 = 0
for row in range(num_rows):
    for col in range(num_columns):
        for dx, dy in directions:
            part1 += check_part1(row, col, dx, dy)
        part2 += check_part2(row, col)


print("Part 1:", part1)
print("Part 2:", part2)
# Part 1: 2493
# Part 2: 1890
