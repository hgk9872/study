# BOJ 1261 - 알고스팟 (골드4)
# bfs

## (1, 1) -> (n, m)으로 가는 bfs를 구현
## 큐에서 .. 우선순위를 두고 큐에 삽입.....
## 만약 벽이 없으면, 먼저 넣고.. 있으면 뒤에 넣는 방식?
from collections import deque

# 가로m, 세로n
m, n = map(int, input().split())

arr = []
for _ in range(n):
    data = list(map(int, input()))
    arr.append(data)

# 방문함수
visited = [[False for col in range(m)] for row in range(n)]

# 상하좌우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
q.append((1, 1, 0)) # 좌표 (1, 1) 부순 횟수 0

while q:
    x, y, count = q.popleft() # 좌표 - (x, y) / 벽 부순 횟수 - count
    if (x, y) == (n, m): # 도착지에 이르면
        print(count)
        break
    for i in range(4): # 상하좌우
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 1 and ny >= 1 and nx <= n and ny <= m and not visited[nx-1][ny-1]:
            if arr[nx-1][ny-1] == 0: # 벽이 없는 경우
                q.appendleft((nx, ny, count)) # count를 증가시키지 않고 우선적으로 처리
                visited[nx-1][ny-1] = True
            else: # 벽인 경우
                q.append((nx, ny, count + 1))
                visited[nx-1][ny-1] = True