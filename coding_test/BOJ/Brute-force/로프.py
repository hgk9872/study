# 백준 2217 - 실버4
# https://www.acmicpc.net/problem/2217
# 그리디

import sys
input = sys.stdin.readline
n = int(input())
data = [int(input()) for _ in range(n)]

data.sort(reverse=True)

answer = []
for i in range(1, n + 1):
    answer.append(data[i-1]* i)

print(max(answer))