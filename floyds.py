n_vertices = int(input('Enter number of vertices: '))
adj_wt_mat = [[0] * n_vertices] * n_vertices
for i in range(n_vertices):
    adj_wt_mat[i] = list(map(int, input().split()))

d = adj_wt_mat.copy()
for k in range(n_vertices):
    for i in range(n_vertices):
        for j in range(n_vertices):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])

print(d)
