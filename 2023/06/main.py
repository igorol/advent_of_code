from math import prod

data = open("input", "r").read().split("\n")
times, distances = [[*map(int, d.split(":")[-1].split())] for d in data]

check_race = lambda time, dist: sum(t * (time - t) > dist for t in range(time))

num_ways_to_win = []
for race_num in range(len(times)):
    this_race_time = times[race_num]
    this_race_dist = distances[race_num]
    num_ways_to_win.append(check_race(this_race_time, this_race_dist))
print("Part 1:", prod(num_ways_to_win))


part2_time = int("".join(map(str, times)))
part2_dist = int("".join(map(str, distances)))
print("Part 2:", check_race(part2_time, part2_dist))
