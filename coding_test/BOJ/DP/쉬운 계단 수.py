# 백준 10844 - 실버1
# https://www.acmicpc.net/problem/10844

# DP 문제인데, 눈에 한 번에 안들어옴... 점화식을 예상함
# 0과 9일 때 한개밖에 못만드는 것도 알았음
# 못푼 이유... -> 2차원 dp리스트인 걸 생각 못함

# 자릿수가 n
n = int(input())

# 열 0~9까지는 마지막 자리의 숫자를 뜻함
# 각 행은 자리수 n
dp = [[0] * 10 for _ in range(n + 1)]

# n = 1인 경우 초기값 세팅
for j in range(1, 10):
    dp[1][j] = 1

if n == 1:
    print(9)
else: # n >= 2인 경우부터 dp 진행
    for i in range(1, n):
        for j in range(10):
            if dp[i][j]: # dp값 0인 경우 제외하기 위함
                if j == 0:
                    dp[i+1][j+1] += dp[i][j]
                elif j == 9:
                    dp[i+1][j-1] += dp[i][j]
                else:
                    dp[i+1][j-1] += dp[i][j]
                    dp[i+1][j+1] += dp[i][j]
    print(sum(dp[n]) % 1000000000)