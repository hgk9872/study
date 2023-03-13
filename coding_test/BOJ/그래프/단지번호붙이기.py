from collections import deque

def bfs(i, j, number):
    q = deque()
    q.append((i, j, number))
    visited[i][j] = True
    graph[i][j] = number

    while q:
        x, y, number = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    graph[nx][ny] = number
                    visited[nx][ny] = True
                    q.append((nx, ny, number))


# n * n 크기의 지도
n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 각 단지의 세대 수 기록을 위한 리스트
answer = []

# 각 단지의 번호
number = 1

visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            bfs(i, j, number) # 좌표, 단지 번호
            number += 1

print(number - 1)

count_list = [0] * (number - 1)

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            index = graph[i][j] - 1
            count_list[index] += 1

count_list.sort()
for i in range(len(count_list)):
    print(count_list[i])