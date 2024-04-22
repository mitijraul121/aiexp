def max_node_hill_climbing(graph):
    max_val = float('-inf')
    max_node = None

    # Find the node with the maximum numeric value
    for node in graph:
        try:
            node_value = float(node)
        except ValueError:
            continue  # Skip non-numeric nodes
        if node_value > max_val:
            max_val = node_value
            max_node = node

    # If no numeric nodes found, return None
    if max_node is None:
        return None

    # Start climbing from the node with the maximum numeric value
    current_node = max_node
    while current_node is not None:
        # Check the value of the current node
        current_value = float(current_node)
        if current_value > max_val:
            max_val = current_value

        # Check if any neighbor has a higher value
        neighbors = graph.get(current_node, [])
        best_neighbor = None
        for neighbor in neighbors:
            neighbor_value = float(neighbor)
            if neighbor_value > max_val:
                best_neighbor = neighbor
                max_val = neighbor_value

        # Move to the best neighbor
        current_node = best_neighbor

    return max_val

# Take graph input from the user
graph = {}
while True:
    node = input("Enter a node (or 'done' to finish): ")
    if node == "done":
        break
    neighbors = input("Enter its neighbors separated by spaces: ").split()
    graph[node] = neighbors

# Call the function with the graph
max_numeric_node = max_node_hill_climbing(graph)
if max_numeric_node is not None:
    print("Maximum numeric value found using hill climbing:", max_numeric_node)
else:
    print("No numeric nodes found in the graph.")
