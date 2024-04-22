import heapq

def Astar(start, goal, graph, heuristic):
    visited = set()
    priority_queue = [(0, start)]
    came_from = {}
    cost_so_far = {start: 0}
    while priority_queue:
        _, current = heapq.heappop(priority_queue)
        if current == goal:
            path = []
            total_cost = 0  # Initialize total cost
            while current in came_from:
                path.append(current)
                total_cost += graph[came_from[current]][current]  # Add edge cost
                current = came_from[current]
            path.append(start)
            return path[::-1], total_cost  # Return path and total cost
        visited.add(current)
        for neighbor, cost in graph[current].items():
            new_cost = cost_so_far[current] + cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic[neighbor]
                heapq.heappush(priority_queue, (priority, neighbor))
                came_from[neighbor] = current
    return None, None  # Goal not reachable
def graph_input():
    graph = {}
    no_edges = int(input("Enter the number of edges: "))
    for _ in range(no_edges):
        u, v, cost = input("Enter the edges (u , v , cost): ").split()
        cost = int(cost)
        if u not in graph:
            graph[u] = {}
        if v not in graph:
            graph[v] = {}
        graph[u][v] = cost
        graph[v][u] = cost
    return graph
def input_heuristic(graph):
    heuristic = {}
    for node in graph.keys():
        heuristic[node] = int(input(f"Enter the value for node {node}: "))
    return heuristic
graph = graph_input()
values = input_heuristic(graph)
start = str(input("Enter the start node: "))  # Corrected input
goal = str(input("Enter the goal node: "))    # Corrected input
path, total_cost = Astar(start, goal, graph, values)
if path:
    print("Path found:", path)
    print("Total cost:", total_cost)
else:
    print("Goal not reachable")
 