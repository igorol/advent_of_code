import numpy as np
import networkx as nx


def get_elevation_array(start_string='S', end_string='E'):
    data = open('input').read().splitlines()
    data = np.array([[ord(char) for char in line] for i, line in enumerate(data)])
    start_pos = tuple([i[0] for i in np.where(data == ord(start_string))])
    end_pos = tuple([i[0] for i in np.where(data == ord(end_string))])
    data[start_pos] = ord('a')
    data[end_pos] = ord('z')
    return data, start_pos, end_pos


def render_path(points, elevation_data):
    for j, line in enumerate(elevation_data):
        for i, _ in enumerate(line):
            print('#' if (j, i) in points else '.', end='')
        print()


elevation, start, end = get_elevation_array()

grid = nx.DiGraph(nx.grid_2d_graph(*elevation.shape))
for node in grid.nodes():
    grid.nodes[node]['elevation'] = elevation[node]

for edge in grid.edges.data():
    diff = grid.nodes.data()[edge[1]]['elevation'] - grid.nodes.data()[edge[0]]['elevation']
    edge[2]['weight'] = diff if diff <= 1 else np.inf

# path_p1 = nx.bellman_ford_path(grid, start, end, 'weight')
path_p1 = nx.dijkstra_path(grid, start, end, 'weight')
render_path(path_p1, elevation)
print('part 1:', len(path_p1) - 1)

origins = [i for i in zip(np.where(elevation == ord('a'))[0], np.where(elevation == ord('a'))[1])]

path_lengths_p2 = []
for origin in origins:
    try:
        path = nx.bellman_ford_path(grid, origin, end, 'weight')
        path_lengths_p2.append(len(path) - 1)
    except nx.exception.NetworkXNoPath:
        pass

print('part 2:', min(path_lengths_p2))

# part 1: 440
# part 2: 439
