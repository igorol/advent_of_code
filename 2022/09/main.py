from math import dist, sqrt


def node_dist(node_a, node_b):
    return dist((node_a.x, node_a.y), (node_b.x, node_b.y))


class Rope:

    MAX_DIST = 1.5

    def __init__(self, x, y, num_tails=1):
        self.num_tails = num_tails
        self.nodes = {i: RopeNode(0, 0) for i in range(self.num_tails + 1)}

    def move(self, move):
        direction, steps = move.split()
        for _ in range(int(steps)):
            self.nodes[0].step(direction)
            _ = [
                self.nodes[tail_id].follow(self.nodes[tail_id - 1])
                for tail_id in range(1, self.num_tails + 1)
            ]


class RopeNode:
    def __init__(self, x, y):
        self.x = 0
        self.y = 0
        self.positions = [(self.x, self.y)]

    def register_position(self):
        self.positions.append((self.x, self.y))

    def step(self, direction):
        match direction:
            case "U":
                self.y += 1
            case "D":
                self.y -= 1
            case "L":
                self.x -= 1
            case "R":
                self.x += 1
            case "UR":
                self.x += 1
                self.y += 1
            case "DR":
                self.x += 1
                self.y -= 1
            case "UL":
                self.x -= 1
                self.y += 1
            case "DL":
                self.x -= 1
                self.y -= 1
        self.register_position()

    def follow(self, other):
        if node_dist(self, other) <= Rope.MAX_DIST:
            pass
        else:
            if self.x == other.x:
                dist = self.y - other.y
                direction = "U" if dist < 0 else "D"
                self.step(direction)
            elif self.y == other.y:
                dist = self.x - other.x
                direction = "L" if dist > 0 else "R"
                self.step(direction)
            else:
                if other.x > self.x and other.y > self.y:
                    self.step("UR")
                elif other.x > self.x and other.y < self.y:
                    self.step("DR")
                elif other.x < self.x and other.y > self.y:
                    self.step("UL")
                else:
                    self.step("DL")


moves = open("input").read().splitlines()
rope_part1 = Rope(0, 0)
_ = [rope_part1.move(move) for move in moves]
print("part 1:", len(set(rope_part1.nodes[1].positions)))

rope_part2 = Rope(0, 0, num_tails=9)
_ = [rope_part2.move(move) for move in moves]
print("part 2:", len(set(rope_part2.nodes[9].positions)))

# part 1: 6090
# part 2: 2566
