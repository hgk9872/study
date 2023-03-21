# 백준 11054 - 골드4
# https://www.acmicpc.net/problem/11054

# 가장 긴 증가하는 부분수열 응용문제..
# 이 응용문제인걸 알았으나, 풀이법이 떠오르지 않음
# 나는 아래처럼 풀었는데, 다른 사람들은 dp값을 두개로 각각 구해서 했음(구글 블로그에 모든 글이 이 방법이다 다들 다른 블로그 글을 참고한듯싶음)

n = int(input())

arr = list(map(int, input().split()))
dp = [1] * n

# 먼저 가장 긴 증가하는 부분수열을 찾아봄
for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# 그리고 감소하는 부분수열에 대해서 dp갱신
for i in range(n):
    for j in range(i):
        if arr[i] < arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))