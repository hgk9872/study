# 백준 5557 골드 5

n = int(input())

# n개의 숫자 배열 중, n-1개까지 수행해야함. 마지막은 결괏값
arr = list(map(int, input().split()))

dp = [[0] * 21 for _ in range(n)]

# 초기값 설정
dp[0][arr[0]] = 1

# n-1번째 dp값까지 갱신(인덱스는 n-2)
for i in range(1, n-1):
    for j in range(21):
        # 그 전에 저장된 dp에서만 실행(0이 아닌 경우)
        if dp[i-1][j]:
            if j + arr[i] <= 20: # 덧셈 연산에 대해 수행
                dp[i][j+arr[i]] += dp[i-1][j]
            if j - arr[i] >= 0:
                dp[i][j-arr[i]] += dp[i-1][j]

print(dp[n-2][arr[-1]])