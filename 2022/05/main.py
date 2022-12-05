def solve(part=2):
    with open("input") as f:
        data = f.readlines()

    stacks = [i.replace("\n", "") for i in data[:8]]
    crates = data[8].replace("\n", "")
    rearrangements = [i.rstrip() for i in data[10:]]

    crates = {
        str(crate_num): [
            stack[crates.index(str(crate_num))]
            for stack in stacks
            if stack[crates.index(str(crate_num))] != " "
        ]
        for crate_num in range(1, 10)
    }

    for action in rearrangements:
        _, quantity, _, origin, _, destination = action.split()
        to_move = crates[origin][: int(quantity)]
        to_move = to_move[::-1] if part == 1 else to_move
        crates[destination] = to_move + crates[destination]
        crates[origin] = crates[origin][len(to_move) :]

    return "".join([i[0] for i in crates.values() if len(i)])


print("part 1:", solve(part=1))
print("part 2:", solve(part=2))
