# 정수 삼각형 p376

# 크기가 n
n = int(input())

# 정수삼각형 그래프면서, 다이나믹 그래프
dp = []
for i in range(n):
    dp.append(list(map(int, input().split())))

# 다이나믹 그래프 갱신
for i in range(1, n):
    m = len(dp[i])
    for j in range(m):
        if j == 0: # 만약 해당 층에서 가장 왼쪽 값인 경우
            prev_left = 0
        else:
            prev_left = dp[i-1][j-1] + dp[i][j]
        if j == m - 1: # 가장 오른쪽 값인 경우
            prev_right = 0
        else:
            prev_right = dp[i-1][j] + dp[i][j]
        dp[i][j] = max(prev_left, prev_right)

result = 0

for j in range(n):
    result = max(result, dp[n-1][j])

print(result)