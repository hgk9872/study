# https://www.acmicpc.net/problem/2292 b2
# 수학

n = int(input())

x = 1
cnt = 1

while n > x:
    x += 6 * cnt
    cnt += 1

print(cnt)