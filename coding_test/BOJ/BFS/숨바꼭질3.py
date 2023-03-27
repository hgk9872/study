from collections import deque
# 이 문제는 가중치가 있는 그래프의 문제이므로, BFS가 아니라 다익스트라로 풀어야 함

# 현재 수빈이의 위치 n, 동생 위치 k
n, k = map(int, input().split())

# 방문함수
visited = [False] * 100001

# 양방향 큐(덱) 초기값 설정
q = deque()
q.append((n, 0)) # 수빈이의 위치에서의 비용은 0
visited[n] = True

while q:
    now, cost = q.popleft()

    # 현재 인덱스가 동생의 위치라면, 결과값 반환 후 종료
    if now == k:
        print(cost)
        exit()
    
    # 현재 위치에서 갈 수 있는 곳 탐색하기
    for next in (now * 2, now + 1, now - 1):
        # 범위를 충족시키고, 방문하지 않았다면
        if 0 <= next < 100001 and not visited[next]:
            if next == now * 2:
                q.appendleft((next, cost)) # 큐 맨 앞에 추가하기
            else:
                q.append((next, cost + 1)) # 비용 +1 증가해서 큐에 삽입
            visited[next] = True