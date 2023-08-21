from itertools import accumulate, cycle

data = [int(i) for i in open("input").read().splitlines()]

print(f"Part 1: {sum(data)}")

seen_frequencies = set([0])
for frequency in accumulate(cycle(data)):
    if frequency in seen_frequencies:
        print(f"Part 2: {frequency}")
        break
    seen_frequencies.add(frequency)
    

