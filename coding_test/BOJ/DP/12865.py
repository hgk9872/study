# BOJ 12865 - 평범한 배낭(0-1 Knapsack problem)

# 물품의 수 n, 최대 수용 무게 k
n, k = map(int, input().split())

# dp 테이블
dp = [0] * (k + 1)

# 물품의 수 n번 반복하면서 DP 테이블 갱신
for _ in range(n):
    # 물품 무게 w, 가치 v
    w, v = map(int, input().split())
    for j in range(k, w-1, -1): # k부터 w까지 역순으로
        dp[j] = max(dp[j], dp[j-w] + v) # 기존값과 추가된 물건가치(v)합 비교

print(dp[-1])

## 역순으로 안하면, if문으로 j < w 조건을 설정해야함