"""Implement A* algorithm. Read directed weighted graph and heuristic
values from user."""

import heapq
from collections import defaultdict

# Read directed, weighted graph from user
def build_graph():
    graph = defaultdict(list)
    num_edges = int(input("Enter number of edges: "))
    print("Enter each edge as: from_node to_node weight")
    for _ in range(num_edges):
        u, v, w = input().split()
        w = int(w)
        graph[u].append((v, w))  # Directed edge
    return graph

# Read heuristic values from user
def read_heuristics():
    heuristics = {}
    num_nodes = int(input("Enter number of nodes with heuristic values: "))
    print("Enter each node and its heuristic value (e.g., A 3):")
    for _ in range(num_nodes):
        node, h = input().split()
        heuristics[node] = int(h)
    return heuristics

# A* Search Algorithm
def a_star_search(graph, heuristics, start, goal):
    open_set = [(heuristics[start], 0, start, [start])]  # (f = g + h, g, node, path)
    visited = set()
    while open_set:
        f, g, current, path = heapq.heappop(open_set)
        if current in visited:
            continue
        visited.add(current)
        if current == goal:
            print("A* Path:", " -> ".join(path))
            print("Total Cost:", g)
            return
        for neighbor, weight in graph[current]:
            if neighbor not in visited:
                new_g = g + weight
                new_f = new_g + heuristics.get(neighbor, float('inf'))
                heapq.heappush(open_set, (new_f, new_g, neighbor, path + [neighbor]))
    print("Goal not reachable.")

# Main
if __name__ == "__main__":
    graph = build_graph()
    heuristics = read_heuristics()
    start = input("Enter the start node: ")
    goal = input("Enter the goal node: ")

    a_star_search(graph, heuristics, start, goal)
