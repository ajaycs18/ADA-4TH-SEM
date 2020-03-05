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
cycle = False
start_vertex = int(input("enter start vertex: "))
stack.append(start_vertex)
while len(stack) > 0:
    node = stack.pop(0)
    if node not in visited:
        print(node, sep=' ')
    else:
        cycle = True
    visited.add(node) 
    if graph.get(node):
        for n in graph.get(node):
            stack.append(n)

if len(visited) == n_vertices:
    print("Connected!")
else:
    print("Not Connected!")

if cycle:
    print("Cycle is present")
else:
    print("Cycle is not present")
