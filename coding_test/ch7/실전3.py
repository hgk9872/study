n, m = list(map(int, input().split()))
array = list(map(int, input().split()))

start = 0
end = max(array)

# 이진탐색 수행
while start <= end:
    sum = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            sum += x - mid
    if sum < m:
        end = mid - 1
    else:
        start = mid + 1
        result = mid
        print(result)