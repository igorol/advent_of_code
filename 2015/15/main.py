import re
from itertools import product

import numpy as np
import pandas as pd


def read_data():
    pattern = r"(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)"
    data = open("input").read().splitlines()
    pantry = pd.DataFrame(
        columns=["capacity", "durability", "flavor", "texture", "calories"]
    )
    for line in data:
        m = re.match(pattern, line)
        ingredient = m.groups()[0]
        capacity, durability, flavor, texture, calories = map(int, m.groups()[1:])
        pantry.loc[ingredient, :] = list(map(int, m.groups()[1:]))
    return pantry


def get_score(quantity, pantry):
    result = max(0, (quantity * pantry["capacity"]).sum())
    result *= max(0, (quantity * pantry["durability"]).sum())
    result *= max(0, (quantity * pantry["flavor"]).sum())
    result *= max(0, (quantity * pantry["texture"]).sum())
    return result


def get_cal_score(quantity, pantry):
    return max(0, (quantity * pantry["calories"]).sum())


properties = read_data()
ingredients = properties.index.to_list()
quantities = [
    opt for opt in product(range(101), repeat=len(ingredients)) if sum(opt) == 100
]

score_p1, score_p2 = 0, 0
for quant in quantities:
    if get_cal_score(quant, properties) == 500:
        score_p2 = max(score_p2, get_score(quant, properties))
    score_p1 = max(score_p1, get_score(quant, properties))

print("part 1:", score_p1)
print("part 2:", score_p2)

# part 1: 13882464
# part 2: 11171160
