# 백준 2559 - 실버3
# https://www.acmicpc.net/problem/2559
# 누적 합, 두 포인터, 슬라이딩 윈도우

n, k = map(int, input().split())

arr = list(map(int, input().split()))

sum_list = [0] * n # 해당 인덱스에 누적합 저장

sum_list[0] = arr[0]
for i in range(1, n):
    sum_list[i] = sum_list[i-1] + arr[i]

temp = []

temp.append(sum_list[k-1]) # 맨 처음 k개의 합
for i in range(1, n-k+1):
    temp.append(sum_list[i+k-1] - sum_list[i-1])

print(max(temp))