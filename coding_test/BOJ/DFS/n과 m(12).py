# 백준 15666 - 실버 2
# https://www.acmicpc.net/problem/15666

def dfs(temp, count):
    if count == m:
        print(*temp)
        return
    
    for i in range(len(arr)):
        if not temp or temp[-1] <= arr[i]: # 빈 배열이거나, 마지막 숫자보다 크거나 같은 경우에만
            temp.append(arr[i])
            dfs(temp, count + 1)
            temp.pop()

n, m = map(int, input().split())
arr = sorted(list(set(map(int, input().split()))))

temp = []

dfs(temp, 0)