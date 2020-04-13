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

def dijkstra(graph, src):
	distance = [float('INF')] * n_vertices
	distance[src] = 0
	selected = [(src, distance[src])]
	curr_vertex = src

	while len(selected) < n_vertices:
		min_vertex, min_dist = -1, float('inf')
		
		# update distances from that vertex
		for neighbour in graph[curr_vertex]:
			vertex, weight = neighbour
			distance[vertex] = min(distance[curr_vertex] + weight, distance[vertex])
			
		# find vertex with min distance
		for vertex in range(n_vertices):
			if distance[vertex] <= min_dist and (vertex, distance[vertex]) not in selected:
				min_vertex, min_dist = vertex, distance[vertex]
		
		# add vertex and minimum distance to selected
		selected.append((min_vertex, min_dist))
		# update curr_vertex
		curr_vertex = min_vertex

	print('Vertex\tDistance')
	[print(vertex, '\t', distance, sep='') for vertex, distance in selected]

# graph = {
# 	0: [(1, 4), (7, 8)],
# 	1: [(0, 4), (7, 11), (2, 8)],
# 	2: [(1, 8), (8, 2), (5, 4), (3, 7)],
# 	3: [(2, 7), (5, 14), (4, 9)],
# 	4: [(3, 9), (5, 10)],
# 	5: [(4, 10), (3, 14), (2, 4), (6, 2)],
# 	6: [(5, 2), (8, 6), (7, 1)],
# 	7: [(6, 1), (8, 7), (1, 11), (0, 8)],
# 	8: [(2, 2), (6, 6), (7, 7)]
# }

dijkstra(graph, int(input('enter source vertex: ')))
