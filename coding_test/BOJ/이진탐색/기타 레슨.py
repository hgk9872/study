# 백준 2343 - 실버1
# https://www.acmicpc.net/problem/2343
# 이분탐색 ... 어렵다

# 크기의 최솟값을 구하는 문제

N, M = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0
left, right = max(arr), sum(arr)
while left <= right:
    mid = (left+right)//2

    # 블루레이에 강의 넣기
    count, sum = 0, 0
    for i in range(N):
        if sum + arr[i] > mid:
            count += 1
            sum = 0
        sum += arr[i]
    if sum:
        count += 1

    if count > M: # 개수가 많다. 크기가 작다 -> 크기를 늘려야 함
        left = mid + 1
    else:
        right = mid - 1
        answer = mid

print(answer)