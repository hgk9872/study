# 백준 7569 - 골드 5
# https://www.acmicpc.net/problem/7569
# 3차원 리스트에 대한 공부
# 최소 며칠이 걸리는지를 계산해서 출력해야 하므로, BFS

# 아래처럼 grpah 작성하지말고,
# graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)] 가 나을듯...

from collections import deque

# 상자의 크기 m, n, h
m, n, h = map(int, input().split())

graph = [[] for _ in range(h)]

for k in range(h):
    graph[k] = [list(map(int, input().split())) for _ in range(n)]

answer = 0

# 위 상자, 아래 상자, (현재상자)상, 하, 좌, 우
dz = [1, -1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]

# 초기값 설정
q = deque()
for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j] == 1: # 토마토가 있는 경우
                q.append((k, i, j, 0)) # 좌표와 현재 일자 저장

while q:
    z, x, y, day = q.popleft()
    answer = max(answer, day)

    # 인접한 상자 확인
    for i in range(6):
        nz = z + dz[i]
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m:
            if graph[nz][nx][ny] == 0: # 익지 않은 토마토가 있는 상자일 때만 전파
                graph[nz][nx][ny] = 1
                q.append((nz, nx, ny, day+1))

# 익지 않은 토마토가 있는지 확인
for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j] == 0: # 익지 않은 토마토가 있다면
                print(-1)
                exit()

print(answer)
