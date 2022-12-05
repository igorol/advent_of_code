def read_grid():
    with open("day3.input", "r") as f:
        grid = [i.rstrip() for i in f.readlines()]
    return grid


def count_trees(this_grid, right=3, down=1):

    max_y, max_x = (len(this_grid), len(this_grid[0]))
    num_trees = 0
    y, x = [0, 0]

    while y < max_y:
        if this_grid[y][x] == "#":
            num_trees += 1
        x += right
        x %= max_x
        y += down

    return num_trees


if __name__ == "__main__":

    s = """..##.......
    #...#...#..
    .#....#..#.
    ..#.#...#.#
    .#...##..#.
    ..#.##.....
    .#.#.#....#
    .#........#
    #.##...#...
    #...##....#
    .#..#...#.#"""

    test_slope = [line.strip() for line in s.split("\n")]
    assert count_trees(test_slope, right=1, down=1) == 2
    assert count_trees(test_slope, right=3, down=1) == 7
    assert count_trees(test_slope, right=5, down=1) == 3
    assert count_trees(test_slope, right=7, down=1) == 4
    assert count_trees(test_slope, right=1, down=2) == 2

    grid = read_grid()
    print("Part 1", count_trees(grid, right=3, down=1))

    sl1 = count_trees(grid, right=1, down=1)
    sl2 = count_trees(grid, right=3, down=1)
    sl3 = count_trees(grid, right=5, down=1)
    sl4 = count_trees(grid, right=7, down=1)
    sl5 = count_trees(grid, right=1, down=2)

    print("Part 2", sl1 * sl2 * sl3 * sl4 * sl5)

