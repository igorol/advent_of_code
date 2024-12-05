import math

data = [l.strip() for l in open("input").readlines()]
rules = [[int(i) for i in item.split("|")] for item in data if "|" in item]
updates = [[int(i) for i in item.split(",")] for item in data if "," in item]


def solve(update, rules, part=1):
    copy = update.copy()
    check_rules = []
    for item in update:
        copy.remove(item)
        these_rules = [rule[1] for rule in rules if rule[0] == item]
        check_rules.append(
            True
            if all([other_update in these_rules for other_update in copy])
            else False
        )

    if part == 1 and all(check_rules):
        return update[int(len(update) / 2)]
    elif part == 2 and not all(check_rules):
        half = math.floor(len(update) / 2)
        for item in update:
            if sum(rule[0] == item and rule[1] in update for rule in rules) == half:
                return item
            else:
                continue
    else:
        return 0


print("Part 1:", sum(solve(update, rules, part=1) for update in updates))
print("Part 2:", sum(solve(update, rules, part=2) for update in updates))

# Part 1: 4959
# Part 2: 4655
