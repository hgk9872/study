# 백준 1697 - 실버1
# https://www.acmicpc.net/problem/1697

# 이동 시, 모든 경우에 비용이 1초 -> bfs 가능
from collections import deque

# 0 <= n, k <= 100000
# 수빈이의 위치 n, 동생의 위치 k
n, k = map(int, input().split())
visited = [False] * 100001
visited[n] = True # 현재 수빈이의 위치 방문처리

# if n == k:
#     print(0)
#     exit()

q = deque()
q.append((n, 0)) # 수빈이의 현재 위치와 걸린 시간

while q:
    x, cost = q.popleft()
    
    # 동생 위치에 도달하면
    if x == k:
        print(cost)
        break

    # 이동가능한 모든 경우의 수에 대해서 이동
    for next in (x-1, x+1, 2*x):
        if 0 <= next <= 100000:
            if not visited[next]: # 아직 이동하지 않은 점에 대해서만
                visited[next] = True
                q.append((next, cost + 1))