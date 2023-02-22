# https://school.programmers.co.kr/learn/courses/30/lessons/43162
# bfs 또는 union_find로 풀 수 있음
# 여기선 union_find로 풀었는데, 마지막 조심

# 노드 x에 대해서 부모(루트)노드를 찾는 함수
def find_parent(parent, x):
    # 현재 자기 노드가 루트가 아닐 경우
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 노드를 합쳐서(하나의 네트워크), 부모 노드를 가장 작은 숫자로 지정
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    
def solution(n, computers):
    
    # 각 네트워크가 속한 부모 노드(루트)를 갖는 리스트 초기화
    parent = [x for x in range(n)]
    
    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if i != j and computers[i][j] == 1: # 자기 자신을 제외한 다른 노드가 같은 네트워크
                union_parent(parent, i, j)
    
    ## 여기까지 하면 1차적으로 union만 했음
    ## 여기서 또 네트워크끼리 결합된 경우를 찾아야 함

    """
    answer = len(set(parent)) 따라서 이 코드 X
    """    
    
    result = []
    
    ## 이 부분 반드시 체크할 것
    for x in parent:
        root = find_parent(parent, x)
        result.append(root)
    
    return len(set(result))