# 백준 2178 - 실버1 
# 가장 기본적인 BFS 문제

from collections import deque

def bfs():
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())

graph = [list(map(int, input())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

# 큐
q = deque()
q.append((0, 0))

bfs()

print(graph[n-1][m-1])