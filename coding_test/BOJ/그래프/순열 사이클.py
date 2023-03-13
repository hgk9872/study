# 백준 10451 실버3
# 재귀 코드가 더 깔끔하지만, 런타임 에러가 발생할 수 있다(발생은 안했음)
from collections import deque

def bfs(i):
    q = deque()
    q.append(i)
    visited[i] = True

    while q:
        now = q.popleft()

        next = arr[now-1]
        if not visited[next]:
            visited[next] = True
            q.append(next)


# 테스트 케이스의 개수
T = int(input())

for _ in range(T):
    n = int(input())

    arr = list(map(int, input().split()))
    visited = [False] * (n + 1)
    count = 0

    for i in range(1, n+1):
        if not visited[i]:
            bfs(i)
            count += 1

    print(count)
