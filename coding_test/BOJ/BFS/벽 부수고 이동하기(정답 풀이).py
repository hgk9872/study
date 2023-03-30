# 백준 2206 - 골드3
# https://www.acmicpc.net/problem/2206
# 3차원 리스트로 공간 하나 늘려서, 한번의 bfs에서 모든 작업 처리
# 내가 만든 vistied함수가 더 깔끔
# visited 함수는 방문처리 + 거리 기록
from collections import deque

n, m = map(int, input().split())

graph = [list(map(int, input())) for _ in range(n)]
# visited = [[[0]*2 for _ in range(m)] for _ in range(n)] 코드보기 어려움
visited = [[] for _ in range(2)]
for i in range(2):
    visited[i] = [[0] * m for _ in range(n)]

# 맨 처음 방문처리 / 0이면 현재 벽을 부수지 않은 상태
visited[0][0][0] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 1e9

def bfs(block, x, y):
    global answer
    q = deque()
    q.append((block, x, y))

    while q:
        block, x, y = q.popleft()

        if x == n-1 and y == m-1:
            answer = min(answer, visited[block][n-1][m-1])
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                # 벽이 아닌 곳
                if graph[nx][ny] == 0 and visited[block][nx][ny] == 0:
                    visited[block][nx][ny] = visited[block][x][y] + 1
                    q.append((block, nx, ny))
                # 벽인 곳
                if graph[nx][ny] == 1 and block == 0: # 아직 벽 부술 기회가 있는 경우
                    visited[1][nx][ny] = visited[0][x][y] + 1
                    q.append((1, nx, ny))

bfs(0, 0, 0)

if answer == 1e9:
    print(-1)
else:
    print(answer)