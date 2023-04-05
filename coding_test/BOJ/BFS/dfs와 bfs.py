from collections import deque

def dfs(now):
    visited[now] = True

    for i in graph[now]:
        if not visited[i]:
            dfs(i)

def bfs(now):
    visited = [False] * (n + 1)
    q = deque()
    q.append(now)
    visited[now] = True

    while q:
        now = q.popleft()
        
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]
print(graph)