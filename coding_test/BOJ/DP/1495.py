# BOJ 1495 - 기타리스트
# 어떤 방식으로 푸는지는 알았으나, 2차원배열로 구현하는 방법을 생각못 함
# 아래는 인터넷에 있는 대부분의 풀이법.. 익히기

# n: 곡의 개수, s: 시작 볼륨 m: 볼륨 상한값
n, s, m = map(int, input().split())
v = list(map(int, input().split()))

dp = [[0] * (m + 1) for _ in range(n + 1)]

# 초기 볼륨값 : 가능한 볼륨의 dp값에 1 표기
dp[0][s] = 1

# v[i] 번째 순서. 앞에서부터 순서대로 진행
for i in range(1, n + 1):
    for j in range(m + 1): # 0부터 최대 m까지만 볼륨 설정할수 있음
        if dp[i-1][j] == 1: # promising
            if j + v[i - 1] <= m: # 상한값을 넘지 않거나
                dp[i][j + v[i - 1]] = 1 # 기존 볼륨에 현재볼륨값 더함
            if j - v[i - 1] >= 0 : # 음수가 아니라면
                dp[i][j - v[i - 1]] = 1

result = -1
# 큰 값을 알기 위해 맨 뒤(큰 값)부터 순회
for i in range(m, -1, -1):
    if dp[n][i] == 1: # 가능한 값이라면,
        result = i
        break

print(result)