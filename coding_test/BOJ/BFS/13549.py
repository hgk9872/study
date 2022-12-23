# 숨바꼭질 3

from collections import deque

visited = [False] * 100001

n, k = map(int, input().split())

# 큐
q = deque()

# 현재 위치 n, count 값
q.append((n, 0))

while q:
    now, count = q.popleft()
    if now == k:
        print(count)
        break
    if (0 <= now * 2 <= 100000) and not visited[now*2]:
        q.appendleft((now*2, count))
        visited[now*2] = True
    for i in (now + 1, now - 1):
        if (0 <= i <= 100000) and not visited[i]:
            q.append((i, count + 1))
            visited[i] = True