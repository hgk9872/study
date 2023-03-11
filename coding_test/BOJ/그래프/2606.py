# 바이러스 - 실버3
# https://www.acmicpc.net/problem/2606

# 이런 문제 주의할 점... parent에서 루트노드를 찾기 위해서는
# parent각 노드번호의 find_parent로 가장 루트를 찾아야함

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 컴퓨터의 수 n
n = int(input())

# 연결되어있는 컴퓨터 쌍의 수 m
m = int(input())

parent = [x for x in range(n + 1)]

graph = [list(map(int, input().split())) for _ in range(m)]

for row in graph:
    union_parent(row[0], row[1])

count = 0
# 1을 제외하고 1번 컴퓨터에 의해 감염된 컴퓨터의 개수 출력
for i in range(2, n + 1):
    if find_parent(i) == 1:
        count += 1

print(count)