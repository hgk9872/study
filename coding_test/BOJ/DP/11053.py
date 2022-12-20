# BOJ 11053 - 가장 긴 증가하는 부분 수열
# DP 기본문제

# 수열 A의 크기 n
n = int(input())

# 수열 A
arr = list(map(int, input().split()))

# dp 테이블
dp = [1] * n

for i in range(n): # 각 수열의 항목에 대해서
    for j in range(i): # 현재 갱신값 i번째 인덱스 전까지 순회
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1) # 기존 dp값에서 가장 큰 값 + 1

print(max(dp))