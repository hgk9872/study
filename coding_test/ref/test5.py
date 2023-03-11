
for i in range(n):
    for j in range(n):

        if i == n-1 and j == n-1:
            print(dp[i][j])
            # break
        # 오른쪽 dp값 갱신
        if j + dp[i][j] < n:
            dp[i][j + dp[i][j]] += dp[]