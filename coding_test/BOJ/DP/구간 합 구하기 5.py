# 백준 11660 - 실버1

# 아이디어가 안 떠올랐던 문제

# NxN 테이블, 합을 구해야하는 횟수 m
n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

data = [list(map(int, input().split())) for _ in range(m)]

# 누적합을 저장한 dp 그래프
dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + graph[i-1][j-1] #인덱스때문에 graph는 xy좌표 하나씩 감소

# 입력받은 각 데이터마다 값 계산
for x1, y1, x2, y2 in data:
    # 누적합 넓이에서 필요없는 부분을 뺀다. 그리고 두 번 뺀 넓이 더해줌
    # 이 부분 잘 이해하기(그림)
    answer = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
    print(answer)