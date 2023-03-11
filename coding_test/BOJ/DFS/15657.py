# n과 m(8)
# https://www.acmicpc.net/problem/15657

n, m = map(int, input().split())
data = sorted(list(map(int, input().split())))

tmp = []

def dfs(cnt, start):
    if cnt == m:
        print(*tmp)
        return
    
    for i in range(start, n):
        tmp.append(data[i])
        dfs(cnt+1, i+1)
        tmp.pop()

dfs(0, 0)
