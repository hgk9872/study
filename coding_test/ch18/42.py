
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
        
# 탑승구 개수 g
g = int(input())

# 비행기의 개수 p
p = int(input())

# 부모 테이블 초기화
parent = [x for x in range(g + 1)]

result = 0
for _ in range(p):
    data = find_parent(parent, int(input()))
    if data == 0:
        break
    union_parent(parent, data, data - 1)
    result += 1

print(result)