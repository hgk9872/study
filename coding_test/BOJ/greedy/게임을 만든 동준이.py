# 백준 2847

n = int(input())

arr = [int(input()) for _ in range(n)]

answer = 0

for i in range(n-2, -1, -1):
    if arr[i] >= arr[i+1]:
        diff = arr[i] - arr[i+1] + 1
        arr[i] = arr[i] - diff
        answer += diff

print(answer)