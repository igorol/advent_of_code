import numpy as np


def conway_life(num_steps, stuck_corners=False):
    grid = np.stack([[*line] for line in open('input').read().splitlines()])
    grid = (grid == '#').astype(int)
    nx, ny = grid.shape
    if stuck_corners:
        grid[0, 0], grid[-1, 0], grid[0, -1], grid[-1, -1] = 1, 1, 1, 1

    for _ in range(num_steps):
        this_grid = grid.copy()
        for i in range(nx):
            for j in range(ny):
                on_lights = (this_grid[max(0, i - 1):min(i + 2, nx + 1), max(0, j - 1):min(j + 2, ny + 1)]).sum()
                if this_grid[i, j]:
                    grid[i, j] = 0 if (on_lights - 1) not in [2, 3] else 1
                else:
                    grid[i, j] = 1 if on_lights == 3 else 0
        if stuck_corners:
            grid[0, 0], grid[-1, 0], grid[0, -1], grid[-1, -1] = 1, 1, 1, 1

    return grid


print('part 1:', (conway_life(100)).sum())
print('part 2:', (conway_life(100, stuck_corners=True)).sum())

# part 1: 768
# part 2: 781
