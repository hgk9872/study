import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수 n, 간선의 개수 m 입력받기
n, m = map(int, input().split())
# 시작 노드 번호 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]
# 방문했는지에 대한 리스트
visited = [False] * (n + 1)
# 최단 거리 테이블 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보 입력받기
for _ in range(m):
    # a->b 간선 비용 c
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    min_idx = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_idx = i
            min_value = distance[i]
    return min_idx

# 다익스트라 알고리즘
def dijkstra(start):
    # 시작노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]: # 시작점에 연결된 모든 간선에 대한 거리 정보 저장
        distance[j[0]] = j[1]
    # 시작점을 제외한 노드들을 돌아가면서 최솟값 갱신
    for i in range(n - 1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            # 기존 거리보다 현재노드를 거쳐서 가는 경로가 더 짧은 경우
            if distance[j[0]] > distance[now] + j[1]:
                distance[j[0]] = distance[now] + j[1]

# 다익스트라 알고리즘 수행
dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("X")
    else:
        print(distance[i])