with open("input") as f:
    instructions = f.read()

print("Part1", instructions.count("(") - instructions.count(")"))


def santa():
    floor = 0
    for index, instruction in enumerate(instructions):
        if instruction == "(":
            move = 1
        else:
            move = -1

        floor += move

        if floor == -1:
            return index + 1

    return None


print("Part2", santa())
