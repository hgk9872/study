# 백준 2146 - 골드3
# https://www.acmicpc.net/problem/2146
# 섬을 라벨링할때, dfs bfs쓸 수 있는데..
# 이렇게 범위가 100 * 100 처럼 큰 경우 dfs쓰지말자.. (런타임에러.. 재귀 스택 초과)

from collections import deque

def bfs(color):
    global answer
    q = deque()

    checked = [[False] * n for _ in range(n)]
    # 해당 color 에 해당하는 모든 좌표를 큐에 넣는다
    for i in range(n):
        for j in range(n):
            if graph[i][j] == color:
                q.append((i, j, 0))
                checked[i][j] = True
    
    # 매 좌표마다 큐에서 뽑아서 다른 섬으로 가는 짧은 거리 갱신
    while q:
        x, y, count = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 벗어나는것부터 제외
            if 0 <= nx < n and 0 <= ny < n:
                # 다른 섬에 도착한 경우
                # if not visited[nx][ny] and graph[nx][ny] > 0: 해도 맞음
                if graph[nx][ny] != color and graph[nx][ny] > 0:
                    answer = min(answer, count)
                    return
                # 최단거리 찾아감
                if graph[nx][ny] == 0 and not checked[nx][ny]:
                    checked[nx][ny] = True
                    q.append((nx, ny, count+1))
            

def bfs_color(i, j, color):
    q = deque()
    q.append((i, j))

    while q:
        x, y = q.popleft()

        graph[x][y] = color

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not changed[nx][ny] and graph[nx][ny] != 0:
                changed[nx][ny] = True
                q.append((nx, ny))

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

changed = [[False] * n for _ in range(n)]
color = 1
# 섬 구분하기
for i in range(n):
    for j in range(n):
        # 아직 구분하지 않은 섬에 대해
        if graph[i][j] == 1 and not changed[i][j]:
            bfs_color(i, j, color) # 섬을 색깔(숫자)로 구분
            color += 1

answer = 1e9
# 각 섬에서 다른 섬으로 가는 거리를 구하기
for i in range(1, color):
    # 각 섬마다 수행
    bfs(i)

print(answer)