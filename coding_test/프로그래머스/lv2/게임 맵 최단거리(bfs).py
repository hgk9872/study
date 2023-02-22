# https://school.programmers.co.kr/learn/courses/30/lessons/1844
# 가장 기본적인 bfs 문제

from collections import deque

def solution(maps):
    # bfs
    # 벽 : 0, 갈수 있는 곳 : 1
    
    # 행렬 크기
    n = len(maps)
    m = len(maps[0])
    
    # 캐릭터 이동 동, 서, 남, 북
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    # 큐 자료구조 생성 및 초기값 할당
    q = deque()
    q.append((0, 0))
    
    # 큐가 빌 때까지 반복
    while q:
        x, y = q.popleft()
        
        # 네 방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위 밖으로 벗어나는지 체크
            if nx < 0 or ny < 0 or nx >= n or ny >= m or maps[nx][ny] == 0:
                continue
            
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx, ny))
            
    # 도달할 방법이 없으면
    if maps[n-1][m-1] == 1:
        return -1
    
    return maps[n-1][m-1]