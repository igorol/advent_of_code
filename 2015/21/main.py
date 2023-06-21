from itertools import product
from collections import namedtuple

Item = namedtuple("Item", ["Name", "Cost", "Damage", "Armor"])
weapons = [
    Item("Dagger", 8, 4, 0),
    Item("Shortsword", 10, 5, 0),
    Item("Warhammer", 25, 6, 0),
    Item("Longsword", 40, 7, 0),
    Item("Greataxe", 74, 8, 0),
]
armors = [
    Item("None", 0, 0, 0),
    Item("Leather", 13, 0, 1),
    Item("Chainmail", 31, 0, 2),
    Item("Splintmail", 53, 0, 3),
    Item("Bandedmail", 75, 0, 4),
    Item("Platemail", 102, 0, 5),
]
rings = [
    Item("None", 0, 0, 0),
    Item("Damage +1", 25, 1, 0),
    Item("Damage +2", 50, 2, 0),
    Item("Damage +3", 100, 3, 0),
    Item("Defense +1", 20, 0, 1),
    Item("Defense +2", 40, 0, 2),
    Item("Defense +3", 80, 0, 3),
]


def play(player, boss):
    while True:
        boss["HP"] -= max(1, (player["Damage"] - boss["Armor"]))
        if boss["HP"] <= 0:
            return "player"
        player["HP"] -= max(1, (boss["Damage"] - player["Armor"]))
        if player["HP"] <= 0:
            return "boss"


boss_start = {"HP": 103, "Damage": 9, "Armor": 2}
you_start = {"HP": 100, "Damage": 0, "Armor": 0}
plays = []
for option in product(weapons, armors, rings, rings):
    if option[2].Name == option[3].Name != "None":
        continue
    your_player = you_start.copy()
    boss_player = boss_start.copy()
    your_player["Armor"] += sum([i.Armor for i in option])
    your_player["Damage"] += sum([i.Damage for i in option])
    gold = sum(i.Cost for i in option)
    plays.append([play(your_player, boss_player), gold])

player_wins = [p for p in plays if p[0] == "player"]
player_looses = [p for p in plays if p[0] == "boss"]
print("part 1:", min(player_wins, key=lambda w: w[1])[1])
print("part 2:", max(player_looses, key=lambda w: w[1])[1])

# part 1: 121
# part 2: 201
