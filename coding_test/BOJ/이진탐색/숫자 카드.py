# 백준 10815 - 실버5
# https://www.acmicpc.net/problem/10815
# 딱 맞는 값을 찾는 문제 (최소, 최대와 구분)

def binary_search(arr, left, right, target):
    while left <= right:
        mid = (left + right)//2

        if arr[mid] == target:
            return 1
        elif target > arr[mid]: # 찾는 값이 오른쪽 부분에 있는 경우
            left = mid + 1
        else: # 왼쪽 부분에 있는 경우
            right = mid - 1
    
    return 0

n = int(input()) # 상근이가 가지고 있는 카드의 수
arr = list(map(int, input().split()))
arr.sort() # 이진탐색은 꼭 정렬되어 있어야 한다!

m = int(input()) # 확인할 카드 수
data = list(map(int, input().split())) # 확인할 카드

answer = []
for i in range(m):
    # data[i]가 arr에 있는지 확인. 있으면 1 리턴, 없으면 0 리턴해서 answer 리스트에 삽입
    answer.append(binary_search(arr, 0, len(arr)-1, data[i]))

print(*answer)