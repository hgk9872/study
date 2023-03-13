# 골드5
# https://www.acmicpc.net/problem/15686
from itertools import combinations
# n * n 크기의 도시, 최대 m개를 뽑았을 때 최대
n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

chicken = []
house_list = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chicken.append((i, j))
        if graph[i][j] == 1:
            house_list.append((i, j))


answer = 1e9

for case in combinations(chicken, m):
    dist = 0
    # 각 집에서 치킨집까지의 거리 계산
    for x1, y1 in house_list:
        near = 100
        for x2, y2 in case:
            near = min(near, abs(x1-x2) + abs(y1-y2))
        dist += near
    answer = min(answer, dist)

print(answer)