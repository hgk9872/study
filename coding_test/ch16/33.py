# 퇴사 

# 퇴사 날짜 n
n = int(input())

# 날마다 상담정보. 걸리는 기간
t = [0] * (n + 1)
# 받을 수 있는 금액
p = [0] * (n + 1)

# 수익을 저장하는 dp 테이블
dp = [0] * (n + 2)

for i in range(1, n + 1):
    x, y = map(int, input().split())
    t[i] = x
    p[i] = y

# dp 테이블 작업
max_val = 0
for i in range(n, 0, -1): # 인덱스가 n 부터 1까지 뒤에서부터 감소
    if i + t[i] > (n+1):
        dp[i] = max_val
    else:
        dp[i] = max(max_val, p[i] + dp[i + t[i]])
        max_val = dp[i]

print(max_val)