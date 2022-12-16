# 이것이 코딩테스트다 - Q 31 금광 : 다이나믹 프로그래밍

T = int(input())

for test in range(T):
    # n * m 크기의 금광
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    # DP 테이블 초기화
    dp = []
    start = 0
    for i in range(n):
        dp.append(array[start:start + m])
        start += m

    # 가장 왼쪽에 있는 열부터 시작(DP테이블의 2열부터)
    for j in range(1, m): # 열
        for i in range(n): # 행
            # 왼쪽 위에서부터 오는 경우
            if i == 0:
                left_up_val = 0
            else:
                left_up_val = dp[i-1][j-1]
            # 바로 왼쪽에서 오는 경우
            left_val = dp[i][j-1]
            # 왼쪽 아래에서 오는 경우
            if i == n - 1:
                left_down_val = 0
            else:
                left_down_val = dp[i+1][j-1]
            dp[i][j] = dp[i][j] + max(left_val, left_down_val, left_up_val)

    result = 0
    # 맨 오른쪽 열의 모든 값들을 비교
    for i in range(n):
        result = max(result, dp[i][m-1])

    print(result)
