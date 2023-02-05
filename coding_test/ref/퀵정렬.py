array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        # 만약 엇갈렸다면 작은 데이터를 피벗과 교체
        if left > right: # right는 pivot보다 작고, left는 pivot보다 큼
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않은 경우 양쪽 데이터를 교환
            array[right], array[left] = array[left], array[right]
    # 분할 이후, 왼쪽 부분과 오른쪽 부분을 각각 퀵소트 수행
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)