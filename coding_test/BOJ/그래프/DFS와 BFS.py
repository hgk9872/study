from collections import deque

def dfs(now):
    visited[now] = True
    print(now, end=" ")

    for i in graph[now]:
        if not visited[i]:
            dfs(i)

def bfs(v):
    visited = [False] * (n + 1)
    # 큐에 시작노드 넣고 bfs 진행
    q = deque()
    q.append(v)
    visited[v] = True

    while q:
        now = q.popleft()
        print(now, end=" ")

        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)


# 정점 개수 n, 간선 개수 m, 시작노드 v
n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 각 노드마다 오름차순 적용해야함
for row in graph:
    row.sort()

# dfs에서 사용할 방문 함수
visited = [False] * (n + 1)
dfs(v)
print()
bfs(v)