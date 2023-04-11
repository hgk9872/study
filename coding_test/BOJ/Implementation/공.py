# https://www.acmicpc.net/problem/1547 브3

# 컵의 위치르 바꾼 횟수 m
m = int(input())

# 초기 공 위치 1번 인덱스에 있음
arr = [0, 1, 0 ,0]

for _ in range(m):
    x, y = map(int, input().split())
    arr[x], arr[y] = arr[y], arr[x]

print(arr.index(1))
