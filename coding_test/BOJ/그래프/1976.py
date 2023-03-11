# 여행 계획에 속한 도시들이 모두 같은 경우 YES

n = int(input()) # 전체 도시의 수 n
m = int(input()) # 여행 계획에 속한 도시의 수 m

# 부모노드
parent = [x for x in range(n+1)]

graph = [list(map(int, input().split())) for _ in range(n)]

plans = list(map(int, input().split()))

# x번 노드의 parent를 찾는다
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    # 작은 숫자가 부모 노드가 됨
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 각 노드마다 부모 노드 찾기

for i in range(n):
    for j in range(i, n):
        if graph[i][j] == 1: # 연결되어 있다면
            union_parent(parent, i+1, j+1)

flag = True
# 여행계획에 있는 노드들 체크하기
for i in range(m-1):
    if find_parent(parent, plans[i]) == find_parent(parent, plans[i+1]):
        continue
    else:
        flag = False
        break

if flag:
    print('YES')
else:
    print('NO')
