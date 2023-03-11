# m개의 바이러스를 활성 상태로
# 조합으로 m개의 바이러스 위치를 구하고
# 그 상태에서 초마다 퍼트린다
# 그리고 bfs의 시간을 측정하고 가장 작은 값 리턴

from itertools import combinations
from collections import deque

# 연구소의 크기 n, 바이러스의 개수 m
n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

# 매 초 count를 편하기 하기 위해 빈 공간(0)을 -1로 바꾼다
for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            graph[i][j] = -1

    
copy = [[0] * n for _ in range(n)]

# 바이러스 위치 좌표 리스트
virus = [(x, y) for x in range(n) for y in range(n) if graph[x][y] == 2]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 100

def bfs(q):
    global answer
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 기존 그래프에 대해서 빈 공간인 경우에만
            if 0 <= nx < n and 0 <= ny < n and copy[nx][ny] == -1:
                copy[nx][ny] = copy[x][y] + 1
                q.append((nx, ny))

    flag = True
    for row in copy:
        # 채워지지 않은 공간이 있따면
        if -1 in row:
            flag = False
            break
    
    # 빈 공간이 없는 경우에만 max값 count
    max_second = 0
    if flag:
        print(copy)
        for row in copy:
            row_max = max(row)
            max_second = max(max_second, row_max)
        answer = min(answer, max_second)
    
        


# 바이러스를 m개를 활성화시키는 모든 경우
for comb in combinations(virus, m):
    # 복사본
    for i in range(n):
        for j in range(n):
            copy[i][j] = graph[i][j]
    # 활성바이러스를 -1. 큐에 삽입
    q = deque()
    for x, y in comb:
        copy[x][y] = 0 
        q.append((x, y))
    bfs(q)

print(answer)