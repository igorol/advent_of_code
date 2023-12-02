from collections import defaultdict
from math import prod

data = open("input").read().splitlines()
max_counts = {"red": 12, "green": 13, "blue": 14}
valid_games, game_powers = [], []

for line in data:
    game_info, game_sets = line.split(":")
    game_id = int(game_info.split()[-1])
    valid_sets, power_counts = [], defaultdict(int)
    for game_set in game_sets.split(";"):
        counts = {}
        for colors in game_set.split(","):
            color_count, color_name = colors.split()
            counts[color_name] = int(color_count)
            power_counts[color_name] = max(power_counts[color_name], int(color_count))

        valid_sets.append(
            all(counts[keys] <= max_counts[keys] for keys in counts.keys())
        )
    if all(valid_sets):
        valid_games.append(game_id)
    game_powers.append(prod(power_counts.values()))

print("Part 1:", sum(valid_games))
print("Part 2:", sum(game_powers))
