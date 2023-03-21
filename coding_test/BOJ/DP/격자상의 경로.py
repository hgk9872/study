# 백준 10164 - 실버1
# https://www.acmicpc.net/problem/10164

# NxM칸, O표시 위치
n, m, k = map(int, input().split())

# 2차원 dp 그래프
dp = [[0] * m for _ in range(n)]

# O표시가 없는 경우
if k == 0:
    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    print(dp[n-1][m-1])
# 있는 경우
else:
    # 먼저, O 표시의 위치를 계산
    x = (k - 1) // m
    y = (k - 1) % m

    # O 표시 위치까지 먼저 거리 계산
    for i in range(x+1):
        for j in range(y+1):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    # 0 표시부터 끝까지
    for i in range(x, n):
        for j in range(y, m):
            if i == x and j == y:
                continue
            elif i == x or j == y:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    answer = dp[x][y]*dp[n-1][m-1]
    print(answer)