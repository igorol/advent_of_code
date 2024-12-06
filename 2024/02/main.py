import numpy as np

data = open("input").read().splitlines()


def check_safety(lst):
    diffs = np.diff(lst)
    return (sorted(lst) == lst or sorted(lst, reverse=True) == lst) and (
        np.abs(diffs).max() < 4 and np.abs(diffs).min() > 0
    )


part_1 = 0
part_2 = 0
for line in data:
    lst = [int(i) for i in line.split()]

    if check_safety(lst):
        part_1 += 1
        part_2 += 1
    else:
        for item in range(len(lst)):
            new_lst = lst.copy()
            new_lst.pop(item)
            if check_safety(new_lst):
                part_2 += 1
                break


print("Part 1:", part_1)
print("Part 2:", part_2)
