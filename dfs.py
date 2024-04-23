def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Taking user input to create the graph
graph = {}
num_vertices = int(input("Enter the number of vertices: "))

for i in range(num_vertices):
    vertex = input(f"Enter vertex {i + 1}: ")
    neighbors = input(f"Enter neighbors of vertex {vertex}: ").split()
    graph[vertex] = neighbors

start_vertex = input("Enter the start vertex for DFS: ")

print("DFS traversal:")
dfs(graph, start_vertex)

""" Input
Enter the number of vertices: 4
Enter vertex 1: A
Enter neighbors of vertex A: B C
Enter vertex 2: B
Enter neighbors of vertex B: A D
Enter vertex 3: C
Enter neighbors of vertex C: A D
Enter vertex 4: D
Enter neighbors of vertex D: B C
Enter the start vertex for DFS: A
"""
