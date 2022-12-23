# 이코테 교재 실전 4 - 미로 탈출
from collections import deque

# 미로의 크기 n, m (행,열)
n, m = map(int, input().split())

arr = []
for _ in range(n):
    data = list(map(int, input()))
    arr.append(data)

# 방문여부 체크 함수
# visited = [[False * (m + 1) for _ in range(n + 1)] -> 이렇게하니까 0으로 초기화됨
visited = [[False for col in range(m + 1)] for _ in range(n + 1)]

# 큐
q = deque()

# (1, 1)에서 시작, count = 1
q.append((1, 1, 1))

# 좌표 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# bfs
while q:
    x, y, count = q.popleft()
    if (x, y) == (n, m):
        print(count)
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >=1 and ny >= 1 and nx <= n and ny <= m:
            if arr[nx-1][ny-1] == 1 and not visited[nx][ny]:
                q.append((nx, ny, count + 1))
                visited[nx][ny] = True