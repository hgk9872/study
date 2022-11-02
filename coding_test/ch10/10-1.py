### 기본적인 서로소 집합 알고리즘
# 루트노드는 부모 노드가 자기 자신
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# union 연산 함수
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수 v, 간선의 개수 e
v, e = map(int, input().split())
# 부모 테이블 초기화 및 부모노드 설정
parent = [0] * (v + 1)
for i in range(1, v + 1):
    parent[i] = i
##### 한번에 parent = [i for i in range(n + 1)] 해도 될듯

# 노드 2개씩 입력받아서 간선의 개수만큼 union 연산 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ', end='')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')