# 백준 18352 - 실버2
# https://www.acmicpc.net/problem/18352
# 특정 도시 X로부터 각 도시들의 최단거리 계산 : 다익스트라
import heapq, sys
input = sys.stdin.readline

n, m, k, start = map(int, input().split())

graph = [[] for _ in range(n + 1)]

INF = 1e9

distance = [INF] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for next in graph[now]:
            cost = dist + 1
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q, (cost, next))

dijkstra(start)

answer = []

for i in range(1, n + 1):
    if distance[i] == k:
        answer.append(i)

if answer:
    for i in range(len(answer)):
        print(answer[i])
else:
    print(-1)