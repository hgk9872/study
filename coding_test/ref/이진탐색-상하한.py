def down_binary(target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] >= target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
    return left

def up_binary(target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] > target:
            right = mid - 1
        elif arr[mid] <= target:
            left = mid + 1
    return left

arr = [1, 2, 3, 3, 3, 4, 5]
left = 0
right = len(arr) - 1

print('index:', down_binary(3))
print('index:', up_binary(3)) # target의 가장 오른쪽값의 다음 값 인덱스가 나온다