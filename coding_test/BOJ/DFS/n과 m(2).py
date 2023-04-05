# 백준 15650 - 실버3
# https://www.acmicpc.net/problem/15650

def dfs(node, length):
    if length == m:
        print(*temp)
        return

    for i in range(node, n + 1):
        if i not in temp:
            temp.append(i)
            dfs(i, length + 1)
            temp.pop()

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열(오름차순)
n, m = map(int, input().split())

temp = []

dfs(1, 0) # 길이