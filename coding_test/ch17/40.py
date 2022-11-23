# 숨바꼭질 p390
# 다익스트라
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

# 전체 헛간 개수 n, 양방향 통로 개수 m
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

q = []
# 1번노드 시작
distance[1] = 0
heapq.heappush(q, (0, 1)) # 최단거리와, 해당 노드 번호

max_val = 0
while q:
    dist, now = heapq.heappop(q)
    # 이미 방문한 노드는 무시
    if dist > distance[now]:
        continue
    # 뽑은 노드로부터 다음으로 갈 수 있는 노드들
    for next in graph[now]:
        next_dist = dist + 1
        if next_dist > distance[next]: # 최단거리가 아닌 경우 무시
            continue
        max_val = max(max_val, next_dist)
        distance[next] = next_dist
        heapq.heappush(q, (next_dist, next))

print(distance)

# 답 출력
max_node = 0
for i in range(1, n+1):
    if distance[i] == max_val:
        max_node = i
        break

print(max_node, max_val, distance.count(max_val))