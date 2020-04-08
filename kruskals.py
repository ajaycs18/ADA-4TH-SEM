edges = int(input("enter number of edges: "))
n_vertices = int(input("enter number of vertices: "))
graph = []
print("enter edges [start] [end] [weight]: ")
for i in range(edges):
    start, end, weight = [int(x) for x in input().split()]
    graph.append((start, end, weight))

def kruskals(graph):
        graph.sort(key=lambda e: e[2])
        included = set()
        for edge in graph:
                if edge[0] not in included or edge[1] not in included:
                        print(edge[0], '->', edge[1], '=', edge[2])
                        included.add(edge[0])
                        included.add(edge[1])
 
kruskals(graph.copy())
