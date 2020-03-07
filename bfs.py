vertices = int(input("enter the number of vertices: "))
adj_matrix = [[0]*vertices] * vertices
visited = [False] * vertices

print("enter the adjacency matrix:")
for i in range(vertices):
    adj_matrix[i] = [int(e) for e in input().split()]

queue = []
queue.append(0) 
visited[0] = True
while len(queue) > 0: 
    node = queue.pop(0)
    print(node, end=' ')
    for i in range(vertices):
        if adj_matrix[node][i] == 1 and not visited[i]:
            visited[i] = True
            queue.append(i)

print()
