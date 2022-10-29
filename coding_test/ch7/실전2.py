n = int(input())
array = list(map(int, input().split()))

m = int(input())
need = list(map(int, input().split()))

array.sort()

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return None

for target in need:
    if binary_search(array, target, 0, n-1) != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')