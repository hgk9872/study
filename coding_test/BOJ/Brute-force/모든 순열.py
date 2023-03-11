# 10974 - 실버3
# https://www.acmicpc.net/problem/10974

n = int(input())

temp = []

def dfs(cnt):
    if cnt == n:
        print(*temp)
        return
    
    for i in range(1, n + 1):
        if i not in temp:
            temp.append(i)
            dfs(cnt+1)
            temp.pop()

dfs(0)