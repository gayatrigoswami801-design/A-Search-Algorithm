def a_star(graph, heuristic, start, goal):

    open_list = [start]
    closed_list = []
    g_cost = {start: 0}
    parent = {start: None}

    while open_list:

        # Find node with minimum f(n)
        current = open_list[0]

        for node in open_list:
            f_current = g_cost[current] + heuristic[current]
            f_node = g_cost[node] + heuristic[node]

            if f_node < f_current:
                current = node

        # Display values
        g = g_cost[current]
        h = heuristic[current]
        f = g + h

        print(f"Visiting {current}: g={g}, h={h}, f={f}")

        # Goal reached
        if current == goal:
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()

            print("\nGoal Reached!")
            print("Optimal Path :", " -> ".join(path))
            print("Total Cost   :", g)

            return

        open_list.remove(current)
        closed_list.append(current)

        # Explore neighbors
        for neighbor, cost in graph[current]:

            if neighbor in closed_list:
                continue

            new_g = g_cost[current] + cost

            if neighbor not in open_list:
                open_list.append(neighbor)
                g_cost[neighbor] = new_g
                parent[neighbor] = current

            elif new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                parent[neighbor] = current

    print("No path found.")


# Graph
graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 2)],
    'D': [('G', 5)],
    'E': [('G', 3)],
    'F': [('G', 1)],
    'G': []
}

# Heuristic values
heuristic = {
    'A': 10,
    'B': 8,
    'C': 6,
    'D': 5,
    'E': 3,
    'F': 1,
    'G': 0
}

# Start and goal
start = 'A'
goal = 'G'

print("===================================")
print("        A* SEARCH ALGORITHM")
print("===================================")
print("Start Node : ", start)
print("Goal Node  : ", goal)
print("-----------------------------------")

a_star(graph, heuristic, start, goal)

print("===================================")