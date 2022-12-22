def santa(floor = 0):
    for index, instruction in enumerate(instructions):
        floor += 1 if instruction == "(" else -1
        if floor == -1:
            return index + 1

    return None


instructions = open("input").read()
print("part1 :", instructions.count("(") - instructions.count(")"))
print("part2 :", santa())
