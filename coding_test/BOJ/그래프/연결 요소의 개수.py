from collections import deque
import sys

input = sys.stdin.readline
def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        now = q.popleft()

        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

# 정점의 개수 n, 간선의 개수 m
n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

# 연결 정보를 담는 그래프
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
count = 0

for i in range(1, n+1):
    if not visited[i]:
        bfs(i)
        count += 1

print(count)