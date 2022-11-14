# 인구 이동 p353
# https://www.acmicpc.net/problem/16234
import sys
from collections import deque
input = sys.stdin.readline

# 크기 N, 인구차 최소 L, 최대 R
n, L, R = map(int, input().split())

# 전체 그래프
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 상하좌우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    global check
    visited[x][y] = 1     # 방문
    # 연합에 대한 좌표정보
    union = []
    union.append((x, y))
    q = deque()
    q.append((x, y))
    # 4가지 방향으로
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 그래프를 벗어나는 경우 다음 순서로
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            # 인구이동에 대한 조건을 만족하는 경우
            diff = abs(graph[nx][ny] - graph[x][y])
            if L <= diff <= R and visited[nx][ny] == 0:
                q.append((nx, ny))
                union.append((nx, ny))
                visited[nx][ny] = 1
                check = 1
    # 연합리스트에서 좌표
    sum = 0
    for x, y in union:
        sum += graph[x][y]
    # 좌표값 갱신
    for x, y in union:
        graph[x][y] = sum // len(union)

day = 0 

while True:
    # 방문정보를 담는 리스트
    visited = [[0] * n for _ in range(n)]
    check = 0
    # 전체 그래프의 모든 원소를 돌아다니면서
    for i in range(n):
        for j in range(n):
            # 아직 방문하지 않은 좌표에 대해 bfs로 탐색
            if visited[i][j] == 0:
                bfs(i, j)
    if check == 0:
        break
    day += 1

print(day)