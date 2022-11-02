# 루트 노드 리턴함수
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 집합을 합치는 함수
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 학생들의 번호 0~n, 연산의 개수 m
n, m = map(int, input().split())

# parent 함수 초기화
parent = [i for i in range(n + 1)]

for i in range(m):
    f, a, b = map(int, input().split())
    if f == 0: # a, b 속한 팀 합침
        union_parent(parent, a, b)
    else: # 같은 팀에 속해있는지 확인
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")