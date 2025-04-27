"""Implement Breadth First Search Algorithm. Read the undirected
unweighted graph from user. """

from collections import defaultdict, deque

# Function to build graph from user input
def build_graph():
    graph = defaultdict(list)
    num_edges = int(input("Enter number of edges: "))
    print("Enter each edge as two space-separated vertices (e.g., A B):")
    for _ in range(num_edges):
        u, v = input().split()
        graph[u].append(v)
        graph[v].append(u)  # because the graph is undirected
    return graph

# Breadth-First Search using queue
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            for neighbor in graph[node]:
                # print(graph[node], end=' ')
                if neighbor not in visited:
                    queue.append(neighbor)

# Main
if __name__ == "__main__":
    graph = build_graph()
    start_node = input("Enter starting node for BFS: ")
    print("BFS traversal:")
    bfs(graph, start_node)