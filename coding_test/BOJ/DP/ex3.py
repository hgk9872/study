# 교재 이코테 DP 실전문제 3 - 개미 전사

# 창고의 개수 n
n = int(input())

# 각 창고에 저장된 식량개수 리스트
k = list(map(int, input().split()))

# dp 테이블
dp = [0] * n

dp[0] = k[0]
dp[1] = max(k[0], k[1])

for i in range(2, n):
    dp[i] = max(k[i] + dp[i - 2], dp[i - 1])

print(dp)