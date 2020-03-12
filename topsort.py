edges = int(input("enter number of edges: "))
n_vertices = int(input("enter number of vertices: "))
neighbours = {}
print("enter edges [start] [end]: ")
for i in range(edges):
    start, end = [int(x) for x in input().split()]
    if not neighbours.get(start):
        neighbours[start] = [end]
    else:
        neighbours[start].append(end)
    
def topOrder(node, visited, stack):
    visited[node] = True

    if neighbours.get(node):
        for n in neighbours[node]:
            if not visited[n]:
                topOrder(n, visited, stack)
    
    stack.append(node)

visited = [False] * 6 
stack = []
for vertex in neighbours.keys():
    if not visited[vertex]:
        topOrder(vertex, visited, stack)
print(stack[::-1])
    
