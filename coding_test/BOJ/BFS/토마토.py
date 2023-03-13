# 백준 7576 - 골드5
# https://www.acmicpc.net/problem/7576
from collections import deque

def bfs():
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))

# m, n : 열, 행
m, n = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = [list(map(int, input().split())) for _ in range(n)]

day = 0

q = deque()
# 초기 토마토가 들어있는 곳을 큐에 삽입
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i, j))

bfs()

max_day = 0
for row in graph:
    if 0 in row:
        print(-1)
        exit()
    
    max_day = max(max_day, max(row))

print(max_day - 1)