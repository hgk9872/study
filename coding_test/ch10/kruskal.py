# 특정 원소가 속한 집합을 찾기(루트노드 찾기)
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기(간선 연결)
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수 v, 간선의 개수 e
v, e = map(int, input().split())
# parent 리스트 초기화
parent = [i for i in range(v + 1)]

# 간선 리스트 입력받기
edges = []
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b)) # 비용순으로 정렬하기 위해 튜플의 첫 번째 원소를 cost로

edges.sort()

result = 0

for edge in edges:
    cost, a, b = edge
    # 루트노드가 같지 않은 경우(사이클이 없는 경우만 계산)
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
