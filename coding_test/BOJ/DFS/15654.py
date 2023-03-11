# n과 m (5)
# https://www.acmicpc.net/problem/15654

n, m = map(int, input().split())
data = sorted(list(map(int, input().split())))
temp = []

def dfs(cnt):
    if cnt == m:
        print(*temp)
        return
    
    for i in range(n):
        if data[i] in temp:
            continue
        temp.append(data[i])
        dfs(cnt+1)
        temp.pop()

dfs(0)