import csv
import heapq
from collections import defaultdict
from google.colab import files
import os

# Function to read directed, weighted graph from a CSV file
def read_graph_from_csv(filepath):
    graph = defaultdict(list)
    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            u, v, w = row['from'], row['to'], int(row['weight'])
            graph[u].append((v, w))  # Directed edge
    return graph

# Function to read heuristic values from CSV
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
            print("Total cost:", g)
            return

        for neighbor, weight in graph[current]:
            if neighbor not in visited:
                new_g = g + weight
                new_f = new_g + heuristics.get(neighbor, float('inf'))
                heapq.heappush(open_set, (new_f, new_g, neighbor, path + [neighbor]))

    print("Goal not reachable.")

# Main function for file upload and running the A* algorithm
def main():
    # Upload graph and heuristic files from your PC
    print("Please upload the graph data CSV file.")
    uploaded_files = files.upload()
    graph_file = next(iter(uploaded_files))  # Get the name of the uploaded file for graph data

    print("Please upload the heuristic data CSV file.")
    uploaded_files = files.upload()
    heuristic_file = next(iter(uploaded_files))  # Get the name of the uploaded file for heuristics

    # Read graph and heuristics from the uploaded files
    graph = read_graph_from_csv(graph_file)
    heuristics = read_heuristics_from_csv(heuristic_file)

    # Ask for start and goal nodes
    start_node = input("Enter start node: ").strip()
    goal_node = input("Enter goal node: ").strip()

    # Perform A* search
    a_star_search(graph, heuristics, start_node, goal_node)

# Run the main function
if __name__ == "__main__":
    main()
