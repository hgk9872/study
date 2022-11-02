from collections import deque

### 사이클이 발생하지 않는 위상 정렬 ###
# 노드의 개수와 간선의 개수 입력받기
n, m = map(int, input().split())

# 입력 차수 리스트 초기화
indegree = [0] * (n + 1)

# 간선 정보를 담는 그래프 초기화
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

# 위상정렬 함수
def topology_sort():
    result = []
    q = deque()

    # 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                result.append(i)