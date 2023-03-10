def find_sue_part1(data, msg):
    for line in data:
        name, items = line.split(":", 1)
        items = [i.strip() for i in items.split(",")]
        if all(item in msg for item in items):
            return name.split(" ")[-1]


def find_sue_part2(data, msg):
    msg_dict = {}
    for line in msg.splitlines():
        item, qty = line.split(":")
        msg_dict[item] = int(qty.strip())

    for line in data:
        name, items = line.split(":", 1)
        items = [i.strip() for i in items.split(",")]
        item_types = [i.split(":")[0] for i in items]
        item_qtys = [int(i.split(":")[-1]) for i in items]
        if all(i in msg_dict.keys() for i in item_types):
            if all(
                (item in ["cats", "trees"] and qty > msg_dict[item])
                or (item in ["pomeranians", "goldfish"] and qty < msg_dict[item])
                or (
                    item not in ["cats", "trees", "pomeranians", "goldfish"]
                    and qty == msg_dict[item]
                )
                for item, qty in zip(item_types, item_qtys)
            ):
                return name.split(" ")[-1]


ticker_tape = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1
"""

aunties = open("input").read().splitlines()

print("part 1:", find_sue_part1(aunties, ticker_tape))
print("part 2:", find_sue_part2(aunties, ticker_tape))

# part 1: 213
# part 2: 323
