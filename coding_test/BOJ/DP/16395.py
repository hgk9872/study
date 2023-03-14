

n, m = map(int, input().split())
graph = [[1], [1, 1]]

for i in range(2, n+1):
    row = []
    for j in range(i+1):
        if j == 0 or j == i:
            row.append(1)
        else:
            row.append(graph[i-1][j-1] + graph[i-1][j])
    graph.append(row)

print(graph[n-1][m-1])