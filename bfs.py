visited = []
queue = []     

def bfs(visited, graph, node): 
    visited.append(node)
    queue.append(node)

    while queue:          
        m = queue.pop(0) 
        print (m, end = " ") 

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


graph = {}
while True:
    node = input("Enter a node (or 'done' to finish): ")
    if node == "done":
        break
    neighbours = input("Enter its neighbours separated by spaces: ").split()
    graph[node] = neighbours

# Driver Code
start_node = input("Enter the starting node: ")
print("Following is the Breadth-First Search:")
bfs(visited, graph, start_node)