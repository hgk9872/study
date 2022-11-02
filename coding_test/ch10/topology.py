from collections import deque

### 사이클이 발생하지 않는 위상 정렬 ###
# 노드의 개수와 간선의 개수 입력받기
v, e = map(int, input().split())

# 진입차수 초기화
indegree = [0] * (v + 1)

# 간선 정보를 담기 위한 그래프(연결 리스트) 초기화
graph = [[] for i in range(v + 1)]

# 방향 그래프의 모든 간선 정보 입력받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) # a -> b 간선
    indegree[b] += 1

# 위상정렬 함수
def topology():
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque()
    
    # 진입차수가 0인 노드를 큐에 삽입 (초기 설정)
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        # 큐에서 꺼낸 후, 결과리스트에 저장
        now = q.popleft()
        result.append(now)
        # 연결된 간선 확인 (사이클이 없다고 가정)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    
    for i in result:
        print(i, end=' ')

topology()