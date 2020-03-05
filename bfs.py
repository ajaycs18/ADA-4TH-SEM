vertices = int(input("enter the number of vertices: "))
adj_matrix = [[0]*vertices] * vertices
visited = [False] * vertices

print("enter the adjacency matrix:")
for i in range(vertices):
    adj_matrix[i] = [int(e) for e in input().split()]

queue = []
queue.append(0) 
while len(queue) > 0: 
    node = queue.pop(0)
    print(node, end=' ')
    for i in range(vertices):
        if adj_matrix[node][i] == 1 and not visited[i]:
            queue.append(i)
    visited[node] = True

print()
'''
   0 1 1 0
   0 0 0 1
   0 1 0 0
   0 0 0 0 
'''
