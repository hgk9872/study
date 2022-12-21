# 교재 이코테 DP 실전문제 2

# 정수 x
x = int(input())

# dp테이블 (정수 범위 1~30000)
dp = [0] * 30001

# 1부터 dp테이블에 최솟값 갱신
# 나눗셈(5, 3, 2) -> 뺄셈 순으로 진행하면 dp값에 최솟값 저장

for i in range(2, 30001):
    if i % 5 == 0:
        dp[i] = min(dp[i-1] + 1, dp[i // 5] + 1)
    elif i % 3 == 0:
        dp[i] = min(dp[i-1] + 1, dp[i // 3] + 1)
    elif i % 2 == 0:
        dp[i] = min(dp[i-1]+ 1, dp[i // 2] + 1)
    else:
        dp[i] = dp[i - 1] + 1

print(dp[1:27])