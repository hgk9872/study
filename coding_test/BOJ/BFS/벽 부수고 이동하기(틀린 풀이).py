# 백준 2206 - 골드3
# https://www.acmicpc.net/problem/2206

# 가장 먼저 떠오르는 풀이...
# 벽 하나를 부술 수 있으므로 하나를 부순 모든 경우에 대해서 비교??
# 근데 골드3 이므로.. 시간초과날 것 같기도 함..
# 일단 풀어보자
# ... 시간초과남
from collections import deque
import copy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph):
    q = deque()
    q.append((0, 0))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if nx == 0 and ny == 0:
                    continue
                if graph[nx][ny] == 0: # 이동할 수 있는 경우
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny))
                
    

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

# 벽 안 부쉈을 때, 최단 거리
copy_graph = copy.deepcopy(graph)
bfs(copy_graph)

answer = graph[n-1][m-1]
# 벽 하나 부수는 모든 케이스에 대해 bfs 처리
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            graph[i][j] = 0
            copy_graph = copy.deepcopy(graph)
            bfs(copy_graph) # 벽 부순 그래프에 대해 bfs 수행
            answer = max(answer, copy_graph[n-1][m-1])
            graph[i][j] = 1

# 이동이 불가능한 경우
if answer == 0:
    print(-1)
else:
    print(answer + 1)