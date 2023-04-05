# 백준 2667 - 실버1
# https://www.acmicpc.net/problem/2667
# 좀 더 단순하고 괜찮은 풀이로 다시 풀어봄

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j, idx):
    q = deque()
    q.append((i, j))
    graph[i][j] += idx # 시작 좌표 방문처리
    count = 1

    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1: # 방문 아직 안한 경우
                    graph[nx][ny] += idx
                    q.append((nx, ny))
                    count += 1

    return count


n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

answer_list = []  # 단지 수 저장을 위한 리스트
idx = 1 # 단지 구분을 위한 변수

# 모든 좌표 순회하며 처리되지 않은 단지에 대해 bfs
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            answer_list.append(bfs(i, j, idx)) # bfs의 리턴값은 해당 단지의 아파트 수
            idx += 1

answer_list.sort()
print(len(answer_list))
for i in range(len(answer_list)):
    print(answer_list[i])