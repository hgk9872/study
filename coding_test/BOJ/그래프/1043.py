# 거짓말
# https://www.acmicpc.net/problem/1043

# 진실을 알고있는 사람이 있는 파티에서는 진실을 말해야 함

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

# 사람 수 n, 파티 수 m
n, m = map(int, input().split())

# 진실을 아는 사람 리스트
data = list(map(int, input().split()))

parent = [x for x in range(n + 1)]

# 파티
party = [list(map(int, input().split())) for _ in range(m)]

if data[0] != 0:
    know = data[1:]
else:
    print(m)
    exit()

for row in party:
    num = row[0]
    # 파티에 한 사람만 있는 경우는 패스
    if num == 1:
        continue
    # 파티에 있는 사람들을 묶는다
    for i in range(1, num):
        union_parent(parent, row[i], row[i+1])

# know 리스트 갱신 -> 각 숫자는 알고있는 집합의 부모노드를 뜻함
know_parent = []
for x in know:
    know_parent.append(find_parent(parent, x))


# 결합결과에 대해서 각 파티마다 체크
count = 0

for row in party:
    x = find_parent(parent, row[1])
    if x not in know_parent:
        count += 1

print(count)