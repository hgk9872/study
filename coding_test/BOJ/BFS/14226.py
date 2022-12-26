# BOJ 14226 - 이모티콘 (골드4)
# BFS
import sys
from collections import deque
input = sys.stdin.readline

# 목표 개수 s
s = int(input())


# 큐
q = deque()
q.append((1, 0, 0)) # 현재 이모티콘 수, 현재 클립보드, 시간(count)

# 방문함수
visited = [[False for _ in range(2001)] for row in range(2001)]

while q:
    now, copy, count = q.popleft()
    if now == s:
        print(count)
        break
    if visited[now][copy]: # 방문했다면
        continue
    visited[now][copy] = True
    # 클립보드에 저장하는 연산
    if 0 <= now <= 1000:
        q.append((now, now, count + 1))
    # 클립보드 값을 붙여넣기 하는 연산
    if 0 <= now <= 1000 and copy != 0:
        q.append((now + copy, copy, count + 1))
    # 하나 지우는 연산
    if 1 <= now <= 1000:
        q.append((now - 1, copy, count + 1))