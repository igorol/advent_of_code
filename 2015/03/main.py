from collections import Counter

with open("input", "r") as f:
    santa_moves = [m for m in f.read()]


def move_santa(pos, move):
    if move == ">":
        pos[0] += 1
    elif move == "<":
        pos[0] -= 1
    elif move == "v":
        pos[1] -= 1
    else:
        pos[1] += 1
    return pos


init_house = [0, 0]
visited_houses = []
visited_houses.append((init_house[0], init_house[1]))
new_pos = init_house

for move in santa_moves:
    new_pos = move_santa(new_pos, move)
    visited_houses.append((new_pos[0], new_pos[1]))

print("Part1", len(set(visited_houses)))

robosanta_moves = santa_moves[1::2]
santa_moves = santa_moves[::2]

init_house = [0, 0]
santa_visited_houses = []
santa_visited_houses.append((init_house[0], init_house[1]))
new_pos = init_house[:]

for move in santa_moves:
    new_pos = move_santa(new_pos, move)
    santa_visited_houses.append((new_pos[0], new_pos[1]))

robo_visited_houses = []
robo_visited_houses.append((init_house[0], init_house[1]))
new_pos = init_house[:]

for move in robosanta_moves:
    new_pos = move_santa(new_pos, move)
    robo_visited_houses.append((new_pos[0], new_pos[1]))

print("Part2", len(set(santa_visited_houses + robo_visited_houses)))
