# 백준 7562 - 실버1
# https://www.acmicpc.net/problem/7562
# 최소 이동이므로, bfs
from collections import deque

def bfs(x, y, a, b):
    q = deque()
    q.append((x, y))
    graph[x][y] = 1 # 방문처리

    while q:
        x, y = q.popleft()

        # 도착
        if x == a and y == b:
            print(graph[x][y] - 1) # 출발점부터 카운트했으므로 하나 빼준다
            return
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < l and 0 <= ny < l:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny))


# 갈 수 있는 8가지 방향에 대한 좌표 설정
dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, -2, -1, 1, 2]

T = int(input())

# 각 테스트케이스마다
for t in range(T):
    l = int(input()) # 체스판의 크기
    x, y = map(int, input().split()) # 현재 나이트의 위치
    a, b = map(int, input().split()) # 이동하려고 하는 칸의 위치

    graph = [[0] * l for _ in range(l)]
    bfs(x, y, a, b)