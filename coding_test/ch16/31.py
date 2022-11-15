# 금광 p375

# 테스트횟수 t
t = int(input())

# 테스트횟수만큼 반복
for test in range(t):
    # n행 m열 크기의 행렬
    n, m = map(int, input().split())

    # 테스트 케이스 리스트
    array = list(map(int, input().split()))

    # 전체 테이블 겸 DP 테이블
    dp = []
    idx = 0
    for i in range(n):
        dp.append(array[idx:idx+m])
        idx += m
    
    # 맨 첫번째 열 이후 다음 열부터..
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위, 왼쪽, 왼쪽 아래 케이스 고려
            # 왼쪽 위 케이스
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            # 바로 왼쪽
            left = dp[i][j-1]
            # 왼쪽 아래
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]
            dp[i][j] = dp[i][j] + max(left_up, left, left_down)

    # 결괏값 출력
    result = 0
    
    # 가장 오른쪽 열에 있는 값중 최댓값 출력
    for i in range(n):
        result = max(result, dp[i][m-1])
    print(result)