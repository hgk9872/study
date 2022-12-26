# BOJ 13913 - 숨바꼭질4
# bfs

# visited를 방문할 때, 리스트에 전에 있었던 위치를 저장하기??

from collections import deque

# 현재 위치 N, 찾는 위치 K
n, k = map(int, input().split())

# 큐 자료구조
q = deque()
count = 0
q.append((n, count)) # 현재 위치와 count 수

# 방문함수
visited = [-1] * 100001

while q:
    now, count = q.popleft()
    if now == k:
        break
    # 모든 케이스마다
    for next in (now - 1, now + 1, now * 2):
        # 범위에 포함되고, 방문하지 않은 경우
        if 0 <= next <= 100000 and visited[next] == -1:
            q.append((next, count + 1))
            visited[next] = now

print(count)

data = []
temp = k
for _ in range(count + 1):
    data.append(temp)
    temp = visited[temp]

data.reverse()

[print(x, end=' ') for x in data]