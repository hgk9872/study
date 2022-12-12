# BOJ 6603 - DFS

def dfs(start, depth):
    if depth == 6:
        print(*result) # unpacking
        return
    for i in range(start, len(S)):
        result[depth] = S[i]
        dfs(i + 1, depth + 1)

# 주어진 리스트에서 6개 뽑음
while True:
    data = list(map(int, input().split()))
    # 집합 S의 원소 개수 k
    k = data[0]
    if k == 0:
        break
    # 주어진 집합 S
    S = data[1:]
    # 시작인덱스 0, depth 0
    result = [0] * 6
    dfs(0, 0)
    print()