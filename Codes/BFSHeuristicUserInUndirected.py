"""Implement Best First Search Algorithm. Read the undirected weighted
graph and the heuristic values from user"""

import heapq
from collections import defaultdict

# Function to read undirected weighted graph from user
def build_graph():
    graph = defaultdict(list)
    num_edges = int(input("Enter number of edges: "))
    print("Enter each edge as: node1 node2 weight")
    for _ in range(num_edges):
        u, v, w = input().split()
        w = int(w)
        graph[u].append((v, w))
        graph[v].append((u, w))  # because it's undirected
    return graph

# Function to read heuristic values
def read_heuristics():
    heuristics = {}
    num_nodes = int(input("Enter number of nodes with heuristic values: "))
    print("Enter node and its heuristic value (e.g., A 3):")
    for _ in range(num_nodes):
        node, h = input().split()
        heuristics[node] = int(h)
    return heuristics

# Best First Search algorithm (Greedy using heuristics only)
def best_first_search(graph, heuristics, start, goal):
    visited = set()
    priority_queue = [(heuristics[start], start)]

    while priority_queue:
        h, current = heapq.heappop(priority_queue)

        if current in visited:
            continue

        print(current, end=' ')
        visited.add(current)

        if current == goal:
            print("\nGoal reached.")
            return

        for neighbor, weight in graph[current]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (heuristics[neighbor], neighbor))

    print("\nGoal not reachable.")

# Main
if __name__ == "__main__":
    graph = build_graph()
    heuristics = read_heuristics()
    start = input("Enter the start node: ")
    goal = input("Enter the goal node: ")

    print("Best First Search traversal:")
    best_first_search(graph, heuristics, start, goal)
