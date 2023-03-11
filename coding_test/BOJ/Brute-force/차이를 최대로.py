# 10819 
# https://www.acmicpc.net/problem/10819
# 배열 크기가 작음 -> 완전탐색 가능
# permutations으로 푸는게 편할듯

from itertools import permutations

n = int(input())
data = list(map(int, input().split()))

max_val = 0
# 매 순열마다 계산
for p in permutations(data, n):
    array_sum = 0
    for i in range(n-1):
        array_sum += abs(p[i] - p[i+1])
    max_val = max(max_val, array_sum)

print(max_val)