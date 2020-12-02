import numpy as np


def count_valid_pwds(pw_list, policy="new"):

    resp = []
    for pw_line in pw_list:
        items = pw_line.split(" ")
        letter, pw = items[1][0], items[-1]
        if policy == "old":
            least = int(items[0].split("-")[0])
            most = int(items[0].split("-")[-1])
            letter_count = pw.count(letter)
            resp.append(most >= letter_count >= least)
        elif policy == "new":
            position_1 = int(items[0].split("-")[0]) - 1
            position_2 = int(items[0].split("-")[-1]) - 1
            resp.append((pw[position_1] == letter) ^ (pw[position_2] == letter))
    return np.sum(resp)


with open("day2.input", "r") as f:
    in_list = [i.rstrip() for i in f.readlines()]

test_list = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]

assert count_valid_pwds(test_list, policy="old") == 2

print("Part 1", count_valid_pwds(in_list, policy="old"))

assert count_valid_pwds(test_list) == 1

print("Part 2", count_valid_pwds(in_list))
