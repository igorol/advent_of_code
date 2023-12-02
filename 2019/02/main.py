def intcode(memory):
    pos = 0
    while memory[pos] != 99:
        code = memory[pos]
        val_1 = memory[memory[pos + 1]]
        val_2 = memory[memory[pos + 2]]
        result_pos = memory[pos + 3]
        if code == 1:
            memory[result_pos] = val_1 + val_2
        elif code == 2:
            memory[result_pos] = val_1 * val_2
        else:
            raise ValueError(f"Invalid opcode: {code}")
        pos += 4
    return memory[0]


def part2(target, memory):
    for noun in range(100):
        for verb in range(100):
            this_memory = memory.copy()
            this_memory[1] = noun
            this_memory[2] = verb
            result = intcode(this_memory)
            if result == target:
                return 100 * noun + verb


memory_safe = list(map(int, open("input", "r").read().split(",")))
this_memory = memory_safe.copy()
this_memory[1] = 12
this_memory[2] = 2

print("Part 1:", intcode(this_memory))
print("Part 2:", part2(19690720, memory_safe))

# Part 1: 9706670
# Part 2: 2552
