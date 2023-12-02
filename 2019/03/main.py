def manhattan_distance(p1, p2):
    """'
    Returns the Manhattan distance between two points.
    """
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def run_wire(rules):
    wire_points = [(0, 0)]
    this_pos = wire_points[0]
    for rule in rules.split(","):
        direction = rule[0]
        distance = int(rule[1:])
        for d in range(1, distance + 1):
            if direction == "U":
                next_pos = (this_pos[0], this_pos[1] + d)
            elif direction == "D":
                next_pos = (this_pos[0], this_pos[1] - d)
            elif direction == "R":
                next_pos = (this_pos[0] + d, this_pos[1])
            else:
                next_pos = (this_pos[0] - d, this_pos[1])
            wire_points.append(next_pos)
        this_pos = next_pos

    return wire_points


wire1_rules, wire2_rules = open("input").read().splitlines()
wire1 = run_wire(wire1_rules)
wire2 = run_wire(wire2_rules)
intersections = set(wire1).intersection(set(wire2))
min_distance = min(
    [manhattan_distance((0, 0), point) for point in intersections if point != (0, 0)]
)

print("Part 1:", min_distance)

min_steps = min(
    [
        wire1.index(point) + wire2.index(point)
        for point in intersections
        if point != (0, 0)
    ]
)

print("Part 2:", min_steps)

# Part 1: 2050
# Part 2: 21666