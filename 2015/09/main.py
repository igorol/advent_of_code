from itertools import permutations

import networkx as nx


def all_distances(lines):
    graph = nx.Graph()
    for line in lines:
        city1, _, city2, _, distance = line.split()
        graph.add_edge(city1, city2, distance=int(distance))
    all_dist = set()
    for trip in permutations(graph.nodes):
        distance = sum(
            graph.get_edge_data(i, j)["distance"] for i, j in zip(trip, trip[1:])
        )
        all_dist.add(distance)
    return all_dist


data = open("input").read().splitlines()
distances = all_distances(data)
print("part 1:", min(distances))
print("part 2:", max(distances))
