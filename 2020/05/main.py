import numpy as np


def get_row(bp):
    return int(bp[:7].replace("F", "0").replace("B", "1"), 2)


def get_col(bp):
    return int(bp[7:].replace("L", "0").replace("R", "1"), 2)


def get_id(bp):
    return 8 * get_row(bp) + get_col(bp)


def get_missing_seat(bp_list):
    seats = [
        int(
            i.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1"), 2
        )
        for i in bp_list
    ]

    seats.sort()
    return seats[np.diff(seats).argmax()] + 1


if __name__ == "__main__":
    assert get_row("FBFBBFFRLR") == 44
    assert get_row("BFFFBBFRRR") == 70
    assert get_row("FFFBBBFRRR") == 14
    assert get_row("BBFFBBFRLL") == 102

    assert get_col("FBFBBFFRLR") == 5
    assert get_col("BFFFBBFRRR") == 7
    assert get_col("FFFBBBFRRR") == 7
    assert get_col("BBFFBBFRLL") == 4

    assert get_id("FBFBBFFRLR") == 357
    assert get_id("BFFFBBFRRR") == 567
    assert get_id("FFFBBBFRRR") == 119
    assert get_id("BBFFBBFRLL") == 820

    with open("input", "r") as f:
        bp_list = [i.rstrip() for i in f.readlines()]

    print("Part 1", np.max([get_id(i) for i in bp_list]))

    print("Part 2", get_missing_seat(bp_list))
