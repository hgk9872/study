# 병사 배치하기 p380
# 전형적인 LIS(가장 긴 증가하는 부분 수열 문제)

n = int(input())

array = list(map(int, input().split()))
array.reverse()

# 최대 count에 대한 DP 리스트
d = [1] * n
max_val = 1

for i in range(1, n):
    for j in range(0, i):
        if array[i] > array[j]:
            d[i] = max(d[i], d[j] + 1)
            if d[i] > max_val:
                max_val = d[i]

print(n - max_val)
