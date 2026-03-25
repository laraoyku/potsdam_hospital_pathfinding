import time
import tracemalloc
import osmnx as ox
import networkx as nx

place_name = "Potsdam, Brandenburg, Germany"

print("Loading graph... this may take a few seconds")
G = ox.graph_from_place(place_name, network_type="drive")

print("Graph loaded successfully!")
print(f"Number of nodes: {len(G.nodes)}")
print(f"Number of edges: {len(G.edges)}")

hospitals = {
    "Klinikum Ernst von Bergmann": (52.4004, 13.0645),
    "Alexianer St. Josefs-Krankenhaus": (52.3996, 13.0442),
    "Protestant Center for Geriatric Medicine": (52.4037, 13.0425),
    "Klinikum Westbrandenburg Standort Potsdam": (52.4027, 13.0648)
}

scenarios = {
    "Potsdam Hauptbahnhof": (52.3917, 13.0666),
    "Innenstadt": (52.3988, 13.0578),
    "Babelsberg": (52.3876, 13.1029),
    "Universitat Potsdam": (52.4011, 13.0119),
    "Bornstedt": (52.4193, 13.0376)
}

def get_nearest_node(graph, coord):
    lat, lon = coord
    return ox.distance.nearest_nodes(graph, lon, lat)

print("\nHospital nodes:")
for hospital_name, coord in hospitals.items():
    node = get_nearest_node(G, coord)
    print(f"{hospital_name} -> nearest node: {node}")

print("\nScenario nodes:")
for scenario_name, coord in scenarios.items():
    node = get_nearest_node(G, coord)
    print(f"{scenario_name} -> nearest node: {node}")

hospital_nodes = {}
for hospital_name, coord in hospitals.items():
    hospital_nodes[hospital_name] = get_nearest_node(G, coord)

def dijkstra_to_nearest_hospital(graph, start_node, hospital_nodes):
    best_hospital = None
    best_distance = float("inf")
    best_path = None

    for hospital_name, hospital_node in hospital_nodes.items():
        try:
            distance = nx.shortest_path_length(graph, start_node, hospital_node, weight="length")
            path = nx.shortest_path(graph, start_node, hospital_node, weight="length")

            if distance < best_distance:
                best_distance = distance
                best_hospital = hospital_name
                best_path = path

        except nx.NetworkXNoPath:
            continue

    return best_hospital, best_distance, best_path

def heuristic(node1, node2):
    y1, x1 = G.nodes[node1]["y"], G.nodes[node1]["x"]
    y2, x2 = G.nodes[node2]["y"], G.nodes[node2]["x"]

    return ((x1 - x2)**2 + (y1 - y2)**2) ** 0.5

def astar_to_nearest_hospital(graph, start_node, hospital_nodes):
    best_hospital = None
    best_distance = float("inf")
    best_path = None

    for hospital_name, hospital_node in hospital_nodes.items():
        try:
            path = nx.astar_path(graph, start_node, hospital_node,
                                heuristic=heuristic, weight="length")

            distance = nx.path_weight(graph, path, weight="length")

            if distance < best_distance:
                best_distance = distance
                best_hospital = hospital_name
                best_path = path

        except nx.NetworkXNoPath:
            continue

    return best_hospital, best_distance, best_path

print("\n=== ALL SCENARIOS ===")

for scenario_name, coord in scenarios.items():
    start_node = get_nearest_node(G, coord)

    tracemalloc.start()
    start_time = time.perf_counter()

    d_hospital, d_distance, _ = dijkstra_to_nearest_hospital(G, start_node, hospital_nodes)

    d_runtime = time.perf_counter() - start_time
    _, d_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    tracemalloc.start()
    start_time = time.perf_counter()

    a_hospital, a_distance, _ = astar_to_nearest_hospital(G, start_node, hospital_nodes)

    a_runtime = time.perf_counter() - start_time
    _, a_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"\nScenario: {scenario_name}")

    print("Dijkstra:")
    print(f"  Hospital: {d_hospital}")
    print(f"  Distance: {d_distance:.2f} m")
    print(f"  Runtime: {d_runtime:.6f} s")
    print(f"  Memory: {d_memory} bytes")

    print("A*:")
    print(f"  Hospital: {a_hospital}")
    print(f"  Distance: {a_distance:.2f} m")
    print(f"  Runtime: {a_runtime:.6f} s")
    print(f"  Memory: {a_memory} bytes")