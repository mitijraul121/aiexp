from queue import PriorityQueue

def greedy_best_first_search(graph, start, goal, heuristic):
    visited = set()
    priority_queue = PriorityQueue()
    priority_queue.put((0, start, []))  # Tuple: (priority, node, path)
    
    while not priority_queue.empty():
        _, current_node, path = priority_queue.get()
        visited.add(current_node)
        
        if current_node == goal:
            return True, path  # Return path if goal is reached
        
        for neighbor, cost in graph[current_node]:
            if neighbor not in visited:
                new_path = path + [(current_node, neighbor, cost)]
                priority_queue.put((heuristic[neighbor], neighbor, new_path))
    
    return False, []  # No path exists

def input_graph():
    graph = {}
    num_edges = int(input("Enter the number of edges: "))
    for _ in range(num_edges):
        u, v, cost = input("Enter edge (start,end ,cost): ").split()
        cost = int(cost)
        
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append((v, cost))
        graph[v].append((u, cost))  # Assuming undirected graph
    return graph

def input_heuristic(graph):
    heuristic = {}
    for node in graph.keys():
        heuristic[node] = int(input(f"Enter heuristic value for node {node}: "))
    return heuristic

def print_path(path):
    print("Path from start to goal:")
    total_cost = 0
    for edge in path:
        print(f"{edge[0]} -> {edge[1]} (Cost: {edge[2]})")
        total_cost += edge[2]
    print("Total cost:", total_cost) 

graph = input_graph()
print(graph)
heuristic_values = input_heuristic(graph)
start = input("Enter the start node: ")
goal = input("Enter the goal node: ")
exists, path = greedy_best_first_search(graph, start, goal, heuristic_values)
if exists:
    print(f"Path exists from {start} to {goal}")
    print_path(path)
else:
    print(f"No path exists from {start} to {goal}")
