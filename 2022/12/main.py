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


def make_graph(elevation_2d_array):
    graph = nx.DiGraph(nx.grid_2d_graph(*elevation_2d_array.shape))
    for node in graph.nodes():
        graph.nodes[node]['elevation'] = elevation_2d_array[node]

    for edge in graph.edges.data():
        diff = graph.nodes.data()[edge[1]]['elevation'] - graph.nodes.data()[edge[0]]['elevation']
        edge[2]['weight'] = diff if diff <= 1 else np.inf
    return graph


def find_shortest_path_length(graph, source, target):
    try:
        return len(nx.bellman_ford_path(graph, source, target, 'weight')) - 1
    except nx.exception.NetworkXNoPath:
        return np.nan


elevation, start, end = get_elevation_array()
grid = make_graph(elevation)

length = find_shortest_path_length(grid, start, end)
print('part 1:', length)

origins = [i for i in zip(np.where(elevation == ord('a'))[0], np.where(elevation == ord('a'))[1])]
lengths = [find_shortest_path_length(grid, origin, end) for origin in origins]
print('part 2:', int(np.nanmin(lengths)))

# part 1: 440
# part 2: 439
