import heapq

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

q = []
# 시작노드로 가는 최단 경로는 cost를 0으로 설정하여, 큐에 삽입
heapq.heappush(q, (0, start))
distance[start] = 0

while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
        continue

    for next, nc in graph[now]:
        if dist + nc < distance[next]:
            distance[next] = dist + nc
            heap
