# 화성 탐사 p388
import heapq
INF = 1e9
# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def explore(n):
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))
    # 최단거리 저장
    distance = [[INF] * n for _ in range(n)]
    # 힙 자료구조
    h = []
    heapq.heappush(h, (graph[0][0], 0, 0))
    distance[0][0] = graph[0][0]
    while h:
        dist, x, y = heapq.heappop(h)
        if distance[x][y] < dist:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if distance[nx][ny] > dist + graph[nx][ny]:
                distance[nx][ny] = dist + graph[nx][ny]
                heapq.heappush(h, (distance[nx][ny], nx, ny))
    
    print(distance[n-1][n-1])


# 테스트 케이스 수
T = int(input())

for test in range(T):
    # 그래프 크기 n
    n = int(input())
    explore(n)
