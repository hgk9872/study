INF = int(1e9)

# 회사 개수 N, 경로 개수 M 입력받기
n, m = map(int, input().split())

# 그래프(2차원 리스트) 생성하고, 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]
# 자기 자신으로 가는 간선 0으로 설정
for a in range(1, n + 1):
    graph[a][a] = 0

# 회사가 연결되는 간선 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 목적지 x 노드, 경유지 k
x, k = map(int, input().split())

distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print("-1")
else:
    print(distance)