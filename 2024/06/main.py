import numpy as np
import matplotlib.pyplot as plt
import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def move(grid, y, x, direction):

    if direction == "north":
        if grid[y - 1, x] == b"#":
            direction = "east"
        else:
            y -= 1
    elif direction == "south":
        if grid[y + 1, x] == b"#":
            direction = "west"
        else:
            y += 1
    elif direction == "west":
        if grid[y, x - 1] == b"#":
            direction = "north"
        else:
            x -= 1
    elif direction == "east":
        if grid[y, x + 1] == b"#":
            direction = "south"
        else:
            x += 1

    if x > nx or y > ny or x < 0 or y < 0:
        raise IndexError

    return y, x, direction

def one(grid, obstacle_x, obstacle_y):
        start = time.time()
        original = grid[obstacle_y, obstacle_x]
        dir = "north"
        if original == b"#":
            return 0
        
        grid[obstacle_y, obstacle_x] = b"#"

        points = [(start_y, start_x)]
        y, x = start_y, start_x
        last_point_in_path, this_point_in_path = False, False
       
        while True:
            try:
                last_point_in_path = this_point_in_path
                y, x, dir = move(grid, y, x, dir)
                this_point_in_path = True if ((y, x) in points) and (last_point_in_path == False) else False
                points.append((y, x))             
            except IndexError:
                return 0
            
            if time.time() - start > 10:
                return 1

        

grid = np.array(
    [list(line.strip()) for line in open("input").readlines()], dtype=np.bytes_
)
start_y, start_x = [i[0] for i in np.where(grid == b"^")]
dir = "north"
ny, nx = grid.shape
points = [(start_y, start_x)]

y, x = start_y, start_x
while True:
    try:
        y, x, dir = move(grid, y, x, dir)
        points.append((y, x))
    except IndexError:
        break

print("Part 1:", len(set(points)))

executor = ThreadPoolExecutor(max_workers=8)
num_obstacles = 0

with ThreadPoolExecutor(max_workers=8) as executor:
    futures, results = [], []
    for obstacle_x in range(nx):
        for obstacle_y in range(ny):
            futures.append(executor.submit(one, grid, obstacle_x, obstacle_y))
    for fut in tqdm.tqdm(as_completed(futures), disable=None, total=len(futures)):
        results.append(fut.result(timeout=30))
    

        
            

print("Part 2:", sum(results))
# Part 1:  5095
# Part 2:  1933
