import numpy as np
from itertools import pairwise
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


class Cave:
    ROCK = "#"
    FALLING_SAND = "+"
    STILL_SAND = "o"
    FREE = "."
    UNAVAILABLE = [ROCK, STILL_SAND, FALLING_SAND]

    def __init__(self, cave_dims=(1000, 300), sand_source=(500, 0), fname="input"):
        self.cave_dims = cave_dims
        self.sand_source = sand_source
        self.fname = fname
        self.cave = self.initialize_cave()
        self.counter = 0
        self.abyss_depth = np.where(self.cave == self.ROCK)[1].max()

    def initialize_cave(self):
        this_cave = np.full(self.cave_dims, self.FREE, dtype=str)
        paths = set(open(self.fname).read().splitlines())
        for path in paths:
            lines = [
                tuple(tuple(map(int, p.split(","))) for p in line)
                for line in pairwise(path.split(" -> "))
            ]
            for line in lines:
                start, end = sorted(line)
                this_cave[start[0]: end[0] + 1, start[1]: end[1] + 1] = self.ROCK
        # import sys
        # sys.exit()
        return this_cave

    def update_cave(self, new, old, stop=False):
        self.cave[new] = self.FALLING_SAND
        self.cave[old] = self.STILL_SAND if stop else self.FREE
        return new, old

    def render_cave(self, fname=None):
        data = self.cave[325:675, :170].T
        cmap = ListedColormap(["silver", "goldenrod", "black", "darkred"])
        map_dict = {"#": 0, "+": 1, ".": 2, "o": 3}
        fig, ax = plt.subplots()
        ax.set_axis_off()
        fig.add_axes(ax)
        ax.matshow(np.vectorize(map_dict.get)(data), vmin=0, vmax=3, cmap=cmap)
        fname = fname if fname is not None else f"part2/frame_{self.counter:08d}"
        fig.savefig(f"grid/{fname}.png", bbox_inches="tight", pad_inches=0, dpi=200)
        plt.close(fig)
        self.counter += 1

    def sand_falls(self, render=False):
        pos = self.sand_source
        self.cave[pos] = self.FALLING_SAND

        if self.cave[pos[0], pos[1] + 1] in self.UNAVAILABLE:
            _, __ = self.update_cave(pos, self.sand_source, stop=True)
            return True

        while True:
            if render:
                self.render_cave()

            if pos[1] > self.abyss_depth:
                return True

            if self.cave[pos[0], pos[1] + 1] not in self.UNAVAILABLE:
                pos, previous_pos = self.update_cave((pos[0], pos[1] + 1), pos)
            elif self.cave[pos[0] - 1, pos[1] + 1] not in self.UNAVAILABLE:
                pos, previous_pos = self.update_cave((pos[0] - 1, pos[1] + 1), pos)
            elif self.cave[pos[0] + 1, pos[1] + 1] not in self.UNAVAILABLE:
                pos, previous_pos = self.update_cave((pos[0] + 1, pos[1] + 1), pos)
            else:
                # self.render_cave()
                _, __ = self.update_cave(pos, pos, stop=True)
                return False

    def part1(self):
        while 1:
            if self.sand_falls():
                break
        return np.count_nonzero(self.cave == self.STILL_SAND)

    def part2(self):
        self.abyss_depth += 2
        self.cave[:, self.abyss_depth + 1] = self.ROCK
        while 1:
            if self.sand_falls(render=False):
                break
        return np.count_nonzero(self.cave == self.STILL_SAND) + 2


print("part 1:", Cave().part1())
print("part 2:", Cave().part2())

# part 1: 578
# part 2: 24377
