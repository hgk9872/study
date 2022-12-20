# BOJ 2655 - 가장 높은 탑 쌓기

# 벽돌의 수
n = int(input())

# 각 벽돌 데이터 인덱스, 밑면, 높이, 무게
arr = [(0, 0, 0, 0)]

# DP 테이블
dp = [0] * (n + 1)

# 각 벽돌의 밑면넓이, 높이, 무게
for i in range(1, n + 1):
    data = list(map(int, input().split()))
    arr.append((i, data[0], data[1], data[2]))

arr.sort(key=lambda x: x[1])  # 밑면 넓이로 오름차순 정렬

# 첫 번째 벽돌부터 시작(밑면넓이로 오름차순 정렬된 상태)
for i in range(1, n + 1):
    for j in range(i): # 이전의 dp값들과 비교
        # 이전의 dp값의 벽돌보다 현재 벽돌의 무게가 큰 경우에만 dp 갱신
        if arr[i][3] > arr[j][3]:
            dp[i] = max(dp[i], dp[j] + arr[i][2])

### 내가 작성한 출력부분 -> 틀림
### 아마 인덱스를 역으로 순회하지 않고 index함수를 써서 그런것 같음 (?)
# max_val = max(dp)
# idx = dp.index(max_val)
# result = []
#
# while True:
#     result.append(idx)
#     max_val -= arr[idx][2] # 현재 누적높이 값에서 index에 해당하는 높이 뺌
#     idx = dp.index(max_val) # 그 다음 누적높이값에 해당하는 index 추출
#     if idx == 0:
#         break
#
# print(len(result))
# for i in result:
#     print(i)

max_value = max(dp)
index = dp.index(max_value)
result = []

while index != 0:
    if max_value == dp[index]:
        result.append(arr[index][0])
        max_value -= arr[index][2]
    index -= 1

result.reverse()
print(len(result))
[print(i) for i in result]