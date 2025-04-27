'''Implement Recursive Depth First Search Algorithm. Read the undirected
 unweighted graph from a .csv file.''' 

import csv
from collections import defaultdict
import os

# Function to read the graph from CSV and build adjacency list
def read_graph_from_csv(filename):
    graph = defaultdict(list)
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            u, v = row
            graph[u].append(v)
            graph[v].append(u)  # because the graph is undirected
    return graph

# Recursive DFS function
def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

# Main logic
if __name__ == "__main__":
    folder = "CSV Files"
    filename = os.path.join(folder, "graph.csv")
    graph = read_graph_from_csv(filename)
    print("DFS traversal starting from node A:")
    dfs(graph, 'A', set())
