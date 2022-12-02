def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a
    
# 집의 수 n, 도로의 수 m
n, m = map(int, input().split())

# parent 초기화
parent = [x for x in range(n)]

# 간선정보
edges = []
for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 비용 순으로 오름차순 정렬
edges.sort()

total = 0
sum = 0

for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        sum += cost
    total += cost

print(total - sum)