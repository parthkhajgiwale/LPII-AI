def bfs(graph, start):
    """Perform Breadth-First Search traversal on the given graph."""
    visited = set()
    queue = [start]
    visited.add(start)

    while queue:
        vertex = queue.pop(0)
        print(vertex, end=' ')
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

# Taking user input to create the graph
graph = {}
num_vertices = int(input("Enter the number of vertices: "))

# Inputting vertices and their neighbors
for i in range(num_vertices):
    vertex = input(f"Enter vertex {i + 1}: ")
    neighbors = input(f"Enter neighbors of vertex {vertex}: ").split()
    graph[vertex] = neighbors

start_vertex = input("Enter the start vertex for BFS: ")

print("BFS traversal:")
bfs(graph, start_vertex)

"""Input
Enter the number of vertices: 4
Enter vertex 1: A
Enter neighbors of vertex A: B C
Enter vertex 2: B
Enter neighbors of vertex B: A D
Enter vertex 3: C
Enter neighbors of vertex C: A D
Enter vertex 4: D
Enter neighbors of vertex D: B C
Enter the start vertex for BFS: A
"""
