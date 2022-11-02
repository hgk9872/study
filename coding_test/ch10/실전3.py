def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# n개의 집, m개의 간선
n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

# 간선 정보 입력을 위한 리스트 생성 및 입력받기
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

result = 0 # 간선 합
max = 0 # 거리가 가장 큰 간선
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        max = cost # 정렬되어 있으므로, 가장 큰 값(마지막)이 max에 들어감

print(result - max)