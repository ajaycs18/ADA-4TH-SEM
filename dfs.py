edges = int(input("enter number of edges: "))
n_vertices = int(input("enter number of vertices: "))
graph = {}
print("enter edges [start] [end]: ")
for i in range(edges):
    start, end = [int(x) for x in input().split()]
    if not graph.get(start):
        graph[start] = [end]
    else:
        graph[start].append(end)

stack = []
visited = set()
start_vertex = int(input("enter start vertex: "))
stack.append(start_vertex)

while len(stack) > 0:
    node = stack.pop()
    if node not in visited:
        print(node, sep=' ')
        visited.add(node) 
    if graph.get(node):
        for n in graph.get(node):
            if n not in visited:
                stack.append(n)

if len(visited) == n_vertices:
    print("Connected!")
else:
    print("Not Connected!")

    
stack = []
visited = [False] * len(graph.keys())
def checkCycle(node, visited, stack):
    visited[node] = True
    stack.append(node)
    hasCycle = False

    for n in graph[node]:
        if visited[n]:
            if n in stack:
                return True 
            else:
                return False
        else:
            hasCycle = checkCycle(n, visited, stack)

    stack.pop()
    return hasCycle

if hasCycle:
    print('cycle present')
else:
    print('cycle absent')
