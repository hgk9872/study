# 백준 2579 - 실버3

n = int(input())

steps = [int(input()) for _ in range(n)]

# 예외처리
if n == 1:
    print(steps[0])
elif n == 2:
    print(steps[0] + steps[1])
elif n == 3:
    print(max(steps[0] + steps[2], steps[1] + steps[2]))
else:
    # 초기값 세팅
    dp = [0] * n

    dp[0] = steps[0]
    dp[1] = steps[0] + steps[1] # 두 번째 계단은 무조건 첫 번째를 밟고 두번째 계단을 오를때 최대
    dp[2] = max(steps[1] + steps[2], steps[0] + steps[2])

    # dp[3] 즉, 4번째 칸부터 최댓값 계산
    for i in range(3, n):
        dp[i] = max(dp[i-2] + steps[i], dp[i-3] + steps[i-1] + steps[i])

    print(dp[n-1])
