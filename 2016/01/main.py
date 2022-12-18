from collections import deque


def solve(part2=False):
    instructions = open("input").read().split(", ")
    headings = deque(["N", "E", "S", "W"])
    pos = (0, 0)
    stops = []
    for instruction in instructions:
        turn = instruction[0]
        steps = int(instruction[1:])
        headings.rotate(-1 if turn == "R" else 1)
        heading = headings[0]
        delta = 1 if heading in ["N", 'E'] else -1

        for _ in range(steps):
            pos = (pos[0], pos[1] + delta) if heading in ["N", 'S'] else (pos[0] + delta, pos[1])
            distance = abs(pos[0]) + abs(pos[1])
            if part2 and pos in stops:
                return distance
            stops.append(pos)

    return distance


print("part 1:", solve())
print('part 2:', solve(part2=True))

# part 1: 161
# part 2: 110
