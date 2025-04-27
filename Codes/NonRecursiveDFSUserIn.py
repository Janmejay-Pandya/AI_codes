"""Implement Non-Recursive Depth First Search Algorithm. Read the
undirected unweighted graph from user."""
from collections import defaultdict

# Function to build graph from user input
def build_graph():
    graph = defaultdict(list)
    num_edges = int(input("Enter number of edges: "))
    print("Enter each edge as two space-separated vertices (e.g., A B):")
    for _ in range(num_edges):
        u, v = input().split()
        graph[u].append(v)
        graph[v].append(u)  # undirected
    return graph

# Non-Recursive DFS using stack
def dfs_non_recursive(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            # Add neighbors in reverse to simulate recursive DFS order
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

# Main
if __name__ == "__main__":
    graph = build_graph()
    start_node = input("Enter starting node for DFS: ")
    print("DFS traversal:")
    dfs_non_recursive(graph, start_node)
