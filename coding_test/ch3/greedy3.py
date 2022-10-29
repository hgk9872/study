# 행, 열 입력받기
n, m = map(int, input().split())

max_value = 0

for i in range(n): # 각 행마다 반복
    data = list(map(int, input().split())) # m개의 데이터 입력받음
    min_value = min(data)
    max_value = max(max_value, min_value)

print(max_value)
