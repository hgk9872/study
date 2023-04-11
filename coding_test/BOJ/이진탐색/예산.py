
n = int(input())
arr = list(map(int, input().split()))
max_val = int(input())

left = 0
right = max(arr)
answer = 0

while left <= right:
    mid = (left+right) // 2

    sum_val = 0
    for i in range(n):
        if arr[i] > mid:
            sum_val += mid
        else:
            sum_val += arr[i]
    
    if sum_val > max_val: # 예산보다 큰 경우
        right = mid - 1
    else:
        answer = mid
        left = mid + 1

print(answer)
    

