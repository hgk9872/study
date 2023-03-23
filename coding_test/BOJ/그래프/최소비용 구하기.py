# 백준 1916 - 골드5
# https://www.acmicpc.net/problem/1916
# 다익스트라
import heapq
import sys

input = sys.stdin.readline
n = int(input())  # 도시의 개수
m = int(input())  # 노선의 개수

graph = [[] for _ in range(n + 1)]

# 거리를 저장하는 distance 리스트
INF = 1e9
distance = [INF] * (n + 1) # visited 리스트 역할을 함. 따라서 큐에 넣을 때 갱신해줘야함

for _ in range(m):
    a, b, cost = map(int, input().split()) # a에서 b로 가는 비용 cost
    graph[a].append((b, cost))

start, dest = map(int, input().split()) # a -> b로 가는 최소비용 구하기

# 우선순위큐
q = []
heapq.heappush(q, (start, 0)) # 초기값 설정, 시작지점은 비용 0
distance[start] = 0

while q:
    now, cost = heapq.heappop(q) # 현재노드, 현재노드까지의 비용

    # 현재노드 비용이 저장된 값보다 크다면 이미 처리된 노드임
    if distance[now] < cost:
        continue
    
    # 인접노드들 확인하기
    for nx, ncost in graph[now]:
        #  현재까지의 거리 + 다음노드 비용이 저장된 값보다 작다면 해당 값으로 갱싱
        if cost + ncost < distance[nx]:
            distance[nx] = cost + ncost
            heapq.heappush(q, (nx, cost + ncost))

print(distance[dest])