edges = int(input("enter number of edges: "))
n_vertices = int(input("enter number of vertices: "))
graph = {}
print("enter edges [start] [end] [weight]: ")
for i in range(edges):
    start, end, weight = [int(x) for x in input().split()]
    if not graph.get(start):
        graph[start] = [(end, weight)]
    else:
        graph[start].append((end, weight))

def prims(graph, startVertex):
	selected = set([startVertex])
	for no_edges in range(len(graph.keys()) - 1):
		end = None
		start = None
		weight = int(10e10)
		for startV in selected:
			for endV in graph[startV]:
				if endV[1] < weight and endV[0] not in selected:
					start, end, weight = startV, endV[0], endV[1] 
		print(f"{start} -> {end} = {weight}")
		selected.add(end)

prims(graph, 1)
