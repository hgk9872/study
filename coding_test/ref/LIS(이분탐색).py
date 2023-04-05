

def binary_search(arr, left, right, target):
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1
    
    return left

arr = [1, 2, 3, 3, 5, 5, 7]
left = 0
right = len(arr) - 1

# 만약 3의 위치를 찾는다면 ?
print(binary_search(arr, left, right, 3)) # 3이 있는 위치 중 가장 왼쪽 인덱스값이 나온다

# 만약 target값으로 4를 대입하면 ?
print(binary_search(arr, left, right, 4)) # 4보다 작은 값에서 가장 큰 값의 바로 오른쪽 인덱스가 나옴

