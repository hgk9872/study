import heapq
import sys
from turtle import distance
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(n + 1)]
# 최단거리 테이블 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    distance[start] = 0
    q = []
    # 시작 노드에 대한 초기값 설정하여 큐에 삽입
    heapq.heappush(q, (0, start))
    while q: # 큐가 빌 때까지 반복
        # 맨 앞 노드 꺼내기
        dist, now = heapq.heappop(q)
        if distance[now] < dist: # 방문 + 이미 처리된 노드라면 무시
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("X")
    else:
        print(distance[i])