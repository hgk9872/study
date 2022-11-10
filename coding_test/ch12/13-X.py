# 치킨 배달 p332
# 입력데이터 적음 -> 완전탐색(구현)

import heapq

# 크기 N*N 도시, 폐업 가게수 M
n, m = map(int, input().split())

# 0: 빈칸, 1: 집, 2: 치킨집
chicken = []
house = []
for r in range(1, n+1):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r,c+1))
        elif data[c] == 2:
            chicken.append((r,c+1))

# 각 집마다의 거리 데이터를 힙에 저장
h = []

for r1, c1 in house: # 각 집마다
    dist = 1000
    for r2, c2 in chicken: # 모든 치킨집의 거리를 구해서 최솟값 저장
        dist = min(dist, abs(r1 - r2) + abs(c1 - c2))
    heapq.heappush(h, dist)

total = 0
# 거리가 작은 순으로 m개 더함
for _ in range(m):
    val = heapq.heappop(h)
    total += val

print(total)