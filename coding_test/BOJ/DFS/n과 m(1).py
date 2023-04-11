# 백준 15649 - 실버3
# https://www.acmicpc.net/problem/15649

def dfs(length, temp):
    if length == m:
        print(*temp)
        return
    
    for i in range(1, n+1):
        if i not in temp:
            temp.append(i)
            dfs(length + 1, temp)
            temp.pop()


# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
n, m = map(int, input().split())

temp = []

dfs(0, temp) # 길이