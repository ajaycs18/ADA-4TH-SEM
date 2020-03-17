vertices = int(input('Enter number of vertices: '))
adj_mat = [[0] * vertices] * vertices
for i in range(vertices):
    adj_mat[i] = list(map(int, input().split()))

trans_close = adj_mat
for k in range(vertices):
    for i in range(vertices):
        for j in range(vertices):
            if trans_close[i][j] == 1:
                continue 
            elif trans_close[i][k] == 1 and trans_close[k][j] == 1:
                trans_close[i][j] = 1

print(trans_close)
