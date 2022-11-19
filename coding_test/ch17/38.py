from pprint import pprint
# 정확한 순위 p387

# 학생 수 n, 성적 비교 수 m
n, m = map(int, input().split())

graph = [[999] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][k] + graph[k][b], graph[a][b])

pprint(graph)
