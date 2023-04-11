# https://www.acmicpc.net/problem/13458 브2
import sys
input = sys.stdin.readline

n = int(input()) # 시험장의 개수 n
arr = list(map(int, input().split()))
b, c = map(int, input().split())

cnt = 0
for i in range(len(arr)):
    num = arr[i]
    if num <= b:
        cnt += 1
    else: # 총 감독관 하나로 부족한 경우
        cnt += 1
        num -= b
        if num % c == 0:
            cnt += (num // c)
        else:
            cnt += (num // c) + 1
print(cnt)

