# 백준 11047 - 실버4
# https://www.acmicpc.net/problem/11047
# 그리디 알고리즘

# 내림차순 정렬 후 큰놈부터 채워넣기..

n, k = map(int, input().split())

data = [int(input()) for _ in range(n)]

data.sort(reverse=True)

count = 0

for i in range(n):
    if data[i] <= k:
        count += k // data[i]
        k = k % data[i]

    # 다 만든 경우
    if k == 0:
        break

print(count)
