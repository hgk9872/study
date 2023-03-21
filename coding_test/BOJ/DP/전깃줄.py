# 백준 2565 - 골드5
# 가장 긴 증가하는 부분수열 유형의 문제

n = int(input())

data = [list(map(int, input().split())) for _ in range(n)]
data.sort()

dp = [1] * n

for i in range(n):
    for j in range(i):
        if data[j][1] < data[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n-max(dp))