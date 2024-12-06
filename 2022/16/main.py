import re

import matplotlib.pyplot as plt
import networkx as nx


def read_data():
    pattern = re.compile(
        r"Valve (..) has flow rate=(\d+); tunnels? leads? to valves? (.*)"
    )

    data = open("test_input").read().splitlines()
    graph = nx.Graph()
    for line in data:
        match = re.findall(pattern, line)
        source_valve = match[0][0]
        flow_rate = int(match[0][1])
        graph.add_node(source_valve, flow_rate=flow_rate, open=False)
        conn_valves = [v.strip() for v in match[0][2].split(",")]
        for c in conn_valves:
            graph.add_edge(source_valve, c)

    fig, ax = plt.subplots()
    nx.draw_networkx(
        graph,
        node_color=[f["flow_rate"] for f in graph.nodes.values()],
        cmap="coolwarm",
        ax=ax,
    )
    fig.savefig("graph_test.png")
    plt.close(fig)
    return graph


def compute_pressure(valve, minute, pressure, max_minute=30):
    for edge in nx.dfs_edges(valves_graph, source=valve, depth_limit=1):
        next_valve = valves_graph.nodes[edge[1]]
        if next_valve["flow_rate"] == 0:
            minute += 1
            if minute > max_minute:
                # yield int(pressure)
                return
            remaining_pressure = compute_pressure(edge[1], minute, pressure)
            try:
                pressure += int(list(remaining_pressure)[0])
            except (TypeError, IndexError):
                # yield int(pressure)
                return
        elif next_valve["flow_rate"] > 0:
            minute += 1
            if minute > max_minute:
                # yield int(pressure)
                return
            if not next_valve["open"]:
                minute += 1
                if minute > max_minute:
                    # yield int(pressure)
                    return
                next_valve["opened"] = True
                pressure += int(next_valve["flow_rate"] * (max_minute - minute))
                remaining_pressure = compute_pressure(edge[1], minute, pressure)
                try:
                    pressure += int(list(remaining_pressure)[0])
                except (TypeError, IndexError):
                    # yield int(pressure)
                    return

    return int(pressure)


valves_graph = read_data()
start_minute, start_pressure, start_valve = 1, 0, "AA"
pressures = compute_pressure(start_valve, start_minute, start_pressure)
print(pressures)
# for pressure in pressures:
#     print(pressure)
# part 1: 1754
# part 2: 2474
#
