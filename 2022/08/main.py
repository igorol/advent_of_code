import numpy as np

data = open("input").read().splitlines()
grid = np.array([[digit for digit in line] for line in data], dtype=np.int8)
nx, ny = grid.shape


def is_visible(line):
    return [
        all(tree > tree_a for tree_a in line[i + 1 :])
        or all(tree > tree_b for tree_b in line[:i])
        for i, tree in enumerate(line)
    ]


def scenic_score(line):
    def _count_trees(sub_line, tree):
        for i, other_tree in enumerate(sub_line):
            if tree <= other_tree:
                return i + 1
        return len(sub_line)

    scores = []
    for i, tree in enumerate(line):
        scores_front = (
            0 if i in [0, len(line) - 1] else _count_trees(line[i - 1 :: -1], tree)
        )
        scores_back = (
            0 if i in [0, len(line) - 1] else _count_trees(line[i + 1 :], tree)
        )
        scores.append(scores_front * scores_back)

    return scores


visibility = (
    np.apply_along_axis(is_visible, 1, grid) | np.apply_along_axis(is_visible, 0, grid),
)
print("part 1:", np.sum(visibility))  # part 1: 1816

scores = np.apply_along_axis(scenic_score, 1, grid) * np.apply_along_axis(
    scenic_score, 0, grid
)
print(scores.shape)
print("part 2:", np.max(scores))  # part 2: 383520
