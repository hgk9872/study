# 위상정렬 기본 코드
# 큐, 진입차수 리스트를 이용한다는 점
from collections import deque

# 노드의 개수와 간선의 개수를 입력받음
v, e = map(int, input().split())

# 모든 노드에 대한 진입차수 리스트
indegree = [0] * (v + 1)

# 각 노드에 연결된 간선 정보를 입력받기
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1 # 진입차수 1 증가

# 위상정렬 함수
def topology_sort():
    result = [] # 알고리즘 수행결과를 담을 리스트
    q = deque()

    # 초기 세팅 - 진입차수가 0인 노드 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        # 큐에서 원소꺼내기
        now = q.popleft()
        result.append(now)
        for next in graph[now]:
            indegree[next] -= 1
            if indegree[next] == 0:
                q.append(next)