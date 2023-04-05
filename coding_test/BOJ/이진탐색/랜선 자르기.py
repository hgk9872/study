# 백준 1654 - 실버2
# https://www.acmicpc.net/problem/1654

# 가지고 있는 랜선 수 k, 필요한 랜선 수 n
k, n = map(int, input().split())

arr = [int(input()) for _ in range(k)]

left = 1
right = max(arr)

answer = 0

while left <= right:
    mid = (left + right)//2

    count = 0
    # 가지고 있는 랜선을 다 자름
    for i in range(k):
        count += arr[i] // mid
    
    if count < n: # 랜선 개수가 부족하면, 더 짧게 잘라야함
        right = mid - 1
    else: # 랜선 개수가 많거나 같은 경우
        left = mid + 1
        answer = mid
    
print(answer)