# 백준 1931 - 실버1 (그리디)
# https://www.acmicpc.net/problem/1931

import sys
input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

# 첫 번째 원소를 먼저 오름차순 정렬해줘야만 함
# 그래야만 종료시간이 같은 경우에 제대로 처리됨 ex. (9, 10) -> (10, 10)
data.sort(key=lambda x:x[0]) 
data.sort(key=lambda x:x[1])

count = 1
end = data[0][1]
for i in range(1, n):
    if data[i][0] >= end:
        count += 1
        end = data[i][1]
print(count)