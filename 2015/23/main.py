def step(line, values):
    instruction = line[0]
    if "," in line[1]:
        line[1] = line[1].replace(",", "")
    if instruction == "hlf":
        values[line[1]] = int(values[line[1]] / 2)
    elif instruction == "tpl":
        values[line[1]] *= 3
    elif instruction == "inc":
        values[line[1]] += 1
    elif (
        (instruction == "jmp")
        or (instruction == "jie" and int(values[line[1]]) % 2 == 0)
        or (instruction == "jio" and int(values[line[1]]) == 1)
    ):
        return int(line[-1]), values
    return 1, values


def solve(values, lines):
    position = 0
    while True:
        try:
            line = lines[position].split()
            offset, values = step(line, values)
            position += offset
        except KeyError:
            break
    return values


data = open("input").read().splitlines()
lines = {k: v for k, v in zip(range(len(data)), data)}

print("part 1:", solve({"a": 0, "b": 0}, lines)["b"])
print("part 1:", solve({"a": 1, "b": 0}, lines)["b"])
