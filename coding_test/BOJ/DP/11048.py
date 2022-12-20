# BOJ 11408 - 이동하기

# 미로의 크기 n, m
n, m = map(int, input().split())

# 주어진 데이터 그래프
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

# dp 테이블
# 하나 크게 하는 이유는 왼쪽, 왼쪽 위, 위 에서 오는 값들의 조건을 주기 번거로움
# 하나 더 크게하여 조건 안주고 모든 좌표에 동일하게 dp값을 갱신할 수 있음
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) \
                   + graph[i - 1][j - 1] # 테이블 크기가 달라서 좌표가 행과 열 한칸씩 땡겨짐

print(dp[n][m])