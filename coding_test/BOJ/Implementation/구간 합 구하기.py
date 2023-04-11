import sys
input = sys.stdin.readline

# 수의 개수 n, 구하는 횟수 m
n, m = map(int, input().split())

arr = list(map(int, input().split()))

for i in range(1, n):
    arr[i] = arr[i-1] + arr[i]

for i in range(m):
    start, end  = map(int, input().split())

    if start == 1:
        print(arr[end-1])
    else: 
        print(arr[end-1] - arr[start-2])
    
    

