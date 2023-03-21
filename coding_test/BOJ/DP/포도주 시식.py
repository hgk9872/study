# 백준 2156 - 실버1
# https://www.acmicpc.net/problem/2156

n = int(input())

arr = [int(input()) for _ in range(n)]
dp = [0] * n

if n == 1:
    print(arr[0])
elif n == 2:
    print(arr[0] + arr[1])
else:
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    dp[2] = max(arr[0]+arr[1], arr[0]+arr[2], arr[1]+arr[2])

    for i in range(3, n):
        dp[i] = max(arr[i]+arr[i-1]+dp[i-3], arr[i]+dp[i-2], dp[i-1])

    print(dp[n-1])