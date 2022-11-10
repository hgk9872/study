# 특정 거리의 도시 찾기 p339

# 최단거리 -> 아마 BFS, 큐 이용

from collections import deque
import sys
input = sys.stdin.readline

# 도시 수 n, 도로 개수 m, 거리 k, 출발 도시번호 x
n, m, k, x = map(int, input().split())

# 2차원 그래프(연결리스트)
graph = [[] for _ in range(n + 1)]

# A -> B 도시로 단뱡향 도로가 존재한다
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 방문여부
visited = [0] * (n + 1)

distance = [0] * (n + 1)

result = []

# 시작 도시 x에서 최단 거리가 k인 모든 도시의 번호를 출력
def shortest_city(x, k):
    visited[x] = 1
    queue = deque()
    queue.append(x)
    while queue: # 큐가 빌때까지 반복 ->
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] != 1: # 방문한 적이 없다면
                visited[i] = 1 # 방문처리
                distance[i] = distance[v] + 1 # 출발노드의 거리정보 +1
                queue.append(i)
                if distance[i] == k:
                    result.append(i)

    result.sort()
    if not result:
        print("-1")
    else:
        for x in result:
            print(x)

shortest_city(x, k)