from collections import deque
## 반복 코드는 제일 나중에,
# 테스트 케이스의 개수
T = int(input())

# 각 테스트마다 실행할 함수(위상정렬 코드)
def topology():
    # 팀의 수 n
    n = int(input())
    
    # 팀 등수 리스트 입력받기
    rank = list(map(int, input().split()))

    # 차수 초기화
    indegree = [0] * (n + 1)
    # 등수 관계를 나타내는 간선 그래프
    graph = [[] for _ in range(n + 1)]
    
    # 1등부터 차수 설정하기 : 1등은 차수가 0
    for i in range(n):
        for j in range(i+1, n):
            graph[rank[i]].append(rank[j])
            indegree[rank[j]] += 1
    
    # 상대적인 등수가 바뀐 쌍의 수 m
    m = int(input())

    for _ in range(m):
        a, b = map(int, input().split())
        if b in graph[a]: # a->b 간선이라면
            graph[a].remove(b)
            indegree[b] -= 1
            graph[b].append(a)
            indegree[a] += 1
        else:
            graph[b].remove(a)
            indegree[a] -= 1
            graph[a].append(b)
            indegree[b] += 1
    
    # 위상정렬을 위한 큐
    q = deque()
    
    # 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    result = []
    cycle = False
    uncertain = False
    # 정상적인 위상정렬은 정확히 노드의 개수만큼 수행됨
    for _ in range(n):
        if len(q) == 0:
            cycle = True
            break
        elif len(q) >= 2:
            uncertain = True
            break

        now = q.popleft()
        result.append(now)
        for next in graph[now]:
            indegree[next] -= 1
            if indegree[next] == 0:
                q.append(next)
    
    if cycle:
        print("IMPOSSIBLE")
    elif uncertain:
        print("?")
    else:
        for x in result:
            print(x, end=' ')
        print()
            
    # print(graph)
    # print(indegree)

for test in range(T):
    topology()
