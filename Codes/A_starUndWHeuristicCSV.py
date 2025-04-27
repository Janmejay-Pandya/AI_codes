""" Implement A* algorithm. Read undirected weighted graph and heuristic
values from a .csv file """
import csv
import heapq
from collections import defaultdict
import os

# Function to read undirected weighted graph from a CSV file
def read_graph_from_csv(filepath):
    graph = defaultdict(list)
    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            u, v, w = row['from'], row['to'], int(row['weight'])
            graph[u].append((v, w))
            graph[v].append((u, w))  # Since it's undirected
    return graph

# Function to read heuristic values from a CSV file
def read_heuristics_from_csv(filepath):
    heuristics = {}
    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            heuristics[row['node']] = int(row['heuristic'])
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
    graph_csv = os.path.join("CSV Files", "graphData2.csv")
    heuristics_csv = os.path.join("CSV Files", "heuristicData2.csv")
    graph = read_graph_from_csv(graph_csv)
    heuristics = read_heuristics_from_csv(heuristics_csv)
    start_node = input("Enter start node: ").strip()
    goal_node = input("Enter goal node: ").strip()
    a_star_search(graph, heuristics, start_node, goal_node)
