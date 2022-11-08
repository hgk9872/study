# 플로이드 워셜 알고리즘 연습
INF = int(1e9)

# 노드의 개수 입력받기
n = int(input())
m = int(input())

# 2차원리스트(그래프) 생성 및 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    graph[i][i] = 0

# 간선에 대한 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            