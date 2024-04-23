def astar(graph, start, goal, heuristic):
    """Perform A* search on the given graph."""
    open_set = {start}
    closed_set = set()
    g_score = {start: 0}
    f_score = {start: heuristic[start]}  # f_score = g_score + heuristic
    came_from = {}  # Keep track of the parent node for each vertex

    while open_set:
        current = min(open_set, key=lambda vertex: f_score[vertex])
        if current == goal:
            return reconstruct_path(came_from, goal)

        open_set.remove(current)
        closed_set.add(current)

        for neighbor in graph[current]:
            if neighbor in closed_set:
                continue

            tentative_g_score = g_score[current] + graph[current][neighbor]
            if neighbor not in open_set or tentative_g_score < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic[neighbor]
                open_set.add(neighbor)

    return None  # If goal not reachable


def reconstruct_path(came_from, current):
    """Reconstruct the path from the goal to the start."""
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]


# Taking user input to create the graph
graph = {}
num_vertices = int(input("Enter the number of vertices: "))

# Inputting vertices and their neighbors with costs
for i in range(num_vertices):
    vertex = input(f"Enter vertex {i + 1}: ")
    neighbors_input = input(f"Enter neighbors of vertex {vertex} and their costs separated by space: ").split()
    neighbors = {}
    for j in range(0, len(neighbors_input), 2):
        neighbor = neighbors_input[j]
        cost = int(neighbors_input[j + 1])
        neighbors[neighbor] = cost
    graph[vertex] = neighbors

start_vertex = input("Enter the start vertex for A* search: ")
goal_vertex = input("Enter the goal vertex for A* search: ")

# Assuming heuristic values are provided by the user
heuristic = {}
for vertex in graph:
    heuristic[vertex] = int(input(f"Enter heuristic value for {vertex}: "))

print("Path found by A* search:")
path = astar(graph, start_vertex, goal_vertex, heuristic)
if path:
    print(" -> ".join(path))
else:
    print("Goal not reachable.")

"""
Enter the number of vertices: 5
Enter vertex 1: A
Enter neighbors of vertex A and their costs separated by space: B 5 C 3
Enter vertex 2: B
Enter neighbors of vertex B and their costs separated by space: D 8
Enter vertex 3: C
Enter neighbors of vertex C and their costs separated by space: D 7
Enter vertex 4: D
Enter neighbors of vertex D and their costs separated by space: E 2
Enter vertex 5: E
Enter neighbors of vertex E and their costs separated by space: 
Enter the start vertex for A* search: A
Enter the goal vertex for A* search: E
Enter heuristic value for A: 10
Enter heuristic value for B: 8
Enter heuristic value for C: 6
Enter heuristic value for D: 4
Enter heuristic value for E: 0
"""
