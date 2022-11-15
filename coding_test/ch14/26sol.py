# 리스트 생성부터 힙으로 구현
import heapq

n = int(input())

h = []

for _ in range(n):
    data = int(input())
    heapq.heappush(h, data)

result = 0

while len(h) != 1:
    card1 = heapq.heappop(h)
    card2 = heapq.heappop(h)
    sum = card1 + card2
    result += sum
    heapq.heappush(h, sum)

print(result)