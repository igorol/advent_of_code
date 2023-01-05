import json


def sum_values(document, ignore_reds=False):
    if isinstance(document, list):
        return sum([sum_values(item, ignore_reds) for item in document])
    if isinstance(document, dict):
        if ignore_reds and "red" in document.values():
            return 0
        return sum([sum_values(value, ignore_reds) for value in document.values()])
    if isinstance(document, int):
        return document
    else:
        return 0


doc = json.load(open("input"))
print("part 1:", sum_values(doc))
print("part 2:", sum_values(doc, ignore_reds=True))

# part 1: 119433
# part 2: 68466
