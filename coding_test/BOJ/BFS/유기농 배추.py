# 백준 1012 - 실버2
# https://www.acmicpc.net/problem/1012
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    q = deque()
    q.append((i, j))
    graph[i][j] = 0 # 방문한 좌표는 0으로 바꾼다

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1: # 방문안한 배추가 있는 곳
                    graph[nx][ny] = 0
                    q.append((nx, ny))

T = int(input())    # 테스트 케이스 개수

for t in range(T):
    # 가로, 세로, 배추 개수
    m, n, k = map(int, input().split())
    
    graph = [[0] * m for _ in range(n)]

    # 배추 위치 추가하기
    for _ in range(k):
        y, x = map(int, input().split())
        graph[x][y] = 1
    
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(i, j)
                cnt += 1
    
    print(cnt)