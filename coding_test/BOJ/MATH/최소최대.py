# BOJ 10818 - 최소, 최대 (브론즈3)
# 수학 
import sys
input = sys.stdin.readline

# 정수의 개수 n
n = int(input())

# 주어진 정수 리스트
arr = list(map(int, input().split()))

# 파이썬 내장함수 안 쓰고 풀기
max_val = arr[0]
min_val = arr[0]

for num in arr[1:]:
    if num >= max_val:
        max_val = num
    elif num <= min_val:
        min_val = num

print(min_val, max_val)
