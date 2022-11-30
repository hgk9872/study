# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

# 여행지의 수 N, 여행 계획에 속한 도시의 수 M
n, m = map(int, input().split())

# 부모 테이블 초기화
parent = [x for x in range(n + 1)]

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            union_parent(parent, i+1, j+1)

# 여행 계획 입력받기
plans = list(map(int, input().split()))

result = True
for i in range(m - 1):
    if find_parent(parent, plans[i]) != find_parent(parent, plans[i+1]):
        result = False

if result:
    print("YES")
else:
    print("NO")
