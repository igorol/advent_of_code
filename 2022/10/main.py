import numpy as np


def fill_signal(data):
    signal = {(cycle_id := 1): 1}
    for line in data:
        num_cycles = len(line := line.split())
        for instruc in line:
            cycle_id += 1
            increment = int(instruc) if instruc.lstrip("-").isnumeric() else 0
            signal[cycle_id] = int(signal[cycle_id - 1]) + increment
    return signal


def signal_strenght(signal, cycle_id):
    return cycle_id * signal[cycle_id]


def render_crt(data, crt_dims=(40, 6)):
    """
    Cycle   1 -> ######################################## <- Cycle  40
    Cycle  41 -> ######################################## <- Cycle  80
    Cycle  81 -> ######################################## <- Cycle 120
    Cycle 121 -> ######################################## <- Cycle 160
    Cycle 161 -> ######################################## <- Cycle 200
    Cycle 201 -> ######################################## <- Cycle 240
    """

    width, height = crt_dims
    crt = ""
    for cycle_id in range(1, (width * height) + 1):
        if abs(signal[cycle_id] - (cycle_id - 1) % width) <= 1:
            crt += "#"
        else:
            crt += "."
        if cycle_id % width == 0:
            crt += "\n"

    print(crt)


data = open("input").read().splitlines()
signal = fill_signal(data)
cycle_ids = [20, 60, 100, 140, 180, 220]
signal_strenghts = {
    cycle_id: signal_strenght(signal, cycle_id) for cycle_id in cycle_ids
}
print("part 1:", sum(signal_strenghts.values()))
print("part 2:")
render_crt(data)
print("BGKAEREZ")  # after reading output

# part1 : 14360
# part2 : BGKAEREZ
