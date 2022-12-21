# 교재 이코테 실전문제 5 - 효율적인 화폐 구성

# 화폐 종류 n가지, 가치의 합 m
n, m = map(int, input().split())

# 화폐 종류를 담는 리스트
arr = []
for _ in range(n):
    arr.append(int(input()))

# dp 테이블
dp = [10001] * (m + 1)

# 초기값 설정 **
dp[0] = 0

for i in range(1, m + 1):
    for unit in arr:
        if (i - unit >= 0) and dp[i - unit] != 10001:
            dp[i] = min(dp[i-unit] + 1, dp[i])

print(dp)