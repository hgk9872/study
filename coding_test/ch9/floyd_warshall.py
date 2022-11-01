INF = int(1e9)

# 노드의 개수 및 간선의 개수 입력받기
n = int(input())
m = int(input())

# 2차원 리스트(그래프)만들고, 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기자신으로 가는 비용 0 으로 초기화
for a in range(1, n + 1):
    graph[a][a] = 0

# 간선정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

