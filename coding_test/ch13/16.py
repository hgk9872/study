# 연구소

# 완전탐색으로 3개를 설치하는 모든 경우의 수(조합)
# 각 경우마다 바이러스에 대해서 DFS(BFS)로 방문처리
# 그리고 행렬에서 0의 최솟값을 저장
from itertools import combinations
import copy
from collections import deque

# 세로길이 n, 가로길이 m
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 벽(0) 좌표
walls = []

for x in range(n):
    for y in range(m):
        if graph[x][y] == 0:
            walls.append((x, y))

# 벽을 3개 세울 수 있는 모든 조합의수
candidates = list(combinations(walls, 3))

result = 0

# 상하좌우 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(graph, x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m or graph[nx][ny] != 0:
            continue
        graph[nx][ny] = 2 # 좀비퍼짐
        dfs(graph, nx, ny)

def bfs(graph, x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m or graph[nx][ny] != 0:
                continue
            q.append((nx, ny))
            graph[nx][ny] = 2

# 벽을 3개 세우는 모든 각각의 경우마다 반복
for candidate in candidates:
    temp = copy.deepcopy(graph)
    # 벽 3개 세우기
    for i in range(3):
        x, y = candidate[i]
        temp[x][y] = 1
    # dfs로 방문(좀비퍼짐)
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 2:
                bfs(temp, i, j)
    # 결과 출력 및 최댓값 저장
    count = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                count += 1
    result = max(result, count)

print(result)