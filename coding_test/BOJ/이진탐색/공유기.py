

# def binary_search(array, left, right):
#     while left <= right:
#         mid = (left + right) // 2
#         current = arr[0]
#         count = 1

#         for i in range(1, len(arr)):
#             if arr[i] >= current + mid: # 사이간격 조건 맞으면
#                 count += 1
#                 current = arr[i]
        
#         # 설치개수가 부족하면 크기를 줄임 // 즉, 조건 자체를 만족시키지 못하는 경우
#         if count < c:
#             right = mid - 1
#         else: # 설치 개수가 같거나 많은 경우. 즉, 설치 개수를 줄여야 하므로, 간격을 더 크게 해야함
#             left = mid + 1
#             answer = mid

