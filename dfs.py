visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
graph = {}
while True:
    node = input("Enter a node (or 'done' to finish): ")
    if node == "done":
        break
    neighbours = input("Enter its neighbours separated by spaces: ").split()
    graph[node] = neighbours

start_node=input("enter the start node:")
print("following is the dfs:")
dfs(visited,graph,start_node)