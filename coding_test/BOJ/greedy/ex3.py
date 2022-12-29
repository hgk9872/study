# 이코테 교재 그리디 실전 3번

# 행렬 n, m
n, m = map(int, input().split())

result = 0

# 각 행마다 반복
for _ in range(n):
    data = list(map(int, input().split()))
    now = min(data)
    # 각 행의 최솟값 중 가장 큰 값을 result에 저장
    result = max(result, now)

print(result)
