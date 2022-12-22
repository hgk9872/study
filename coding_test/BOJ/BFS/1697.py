# BOJ 1697 - 숨바꼭질(실버1)
# bfs
from collections import deque

# 현재 위치 n, 찾는 위치 k
n, k = map(int, input().split())

# 방문함수
visited = [False] * 100001

# 큐 생성 및 초기값 설정
q = deque()

# 현재 위치 n과 카운트값을 큐에 삽입
q.append((n, 0))

# 반복
while q:
    now, cnt = q.popleft()
    if now == k:
        print(cnt)
        break
    # 이동할 수 있는 케이스 3가지
    for i in (now - 1, now + 1, now * 2):
        if (0 <= i <= 100000) and not visited[i]:
            q.append((i, cnt + 1))
            visited[i] = True