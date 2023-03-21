# 백준 11727 실버3

n = int(input())

dp = [0] * (n + 1)

if n == 1:
    print(1)
elif n == 2:
    print(3)
else:
    # 초기값 세팅
    dp[1] = 1   # 2x1 직사각형 dp값
    dp[2] = 3   # 2x2
    
    # 2x3 크기부터 dp값 갱신
    for i in range(3, n + 1):
        dp[i] = (dp[i-1] + dp[i-2]*2) % 10007
    
    print(dp[n])
