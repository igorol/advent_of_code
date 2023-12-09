data = open("input").read().split("\n\n")


seeds = list(map(int, data[0].split(":")[1].split()))
maps = [data[1:][m].split("\n\n") for m in range(0, len(data[1:]))]
maps = [
    [[*map(int, ranges.split())] for ranges in m[0].split(":")[-1].split("\n")[1:]]
    for m in maps
]

part1_location = float("inf")
for this_seed in seeds:
    for this_map in maps:
        for dest_rng_start, src_rng_start, rng_len in this_map:
            if src_rng_start <= this_seed < src_rng_start + rng_len:
                this_seed = dest_rng_start + this_seed - src_rng_start
                break
    part1_location = min(part1_location, this_seed)

print("Part 1:", part1_location)


part2_location = 0
seed_pairs = [(seeds[i], seeds[i] + seeds[i + 1] - 1) for i in range(0, len(seeds), 2)]

while True:
    result = part2_location
    for this_map in reversed(maps):
        for dest_rng_start, src_rng_start, rng in this_map:
            if dest_rng_start <= result < dest_rng_start + rng:
                result = src_rng_start + result - dest_rng_start
                break
    if any(seed_pair[0] <= result <= seed_pair[1] for seed_pair in seed_pairs):
        print("Part 2:", part2_location)
        break
    part2_location += 1
