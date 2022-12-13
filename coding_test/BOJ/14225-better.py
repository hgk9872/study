# zeebraa00님의 코드

n = int(input())
num = list(map(int,input().split()))
visited = [0]*10000000

def dfs(idx,sum) :
    if idx == n :
       return
    sum += num[idx]
    visited[sum] = 1
    dfs(idx+1, sum)             # 현재 숫자를 부분수열에 포함할 때
    dfs(idx+1, sum-num[idx])    # 현재 숫자를 부분수열에 포함하지 않을 때

dfs(0,0)
print(visited[1:].index(0)+1)
