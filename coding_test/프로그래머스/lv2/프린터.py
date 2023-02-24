# https://school.programmers.co.kr/learn/courses/30/lessons/42587

from collections import deque

def solution(priorities, location):
    
    # priorities를 enumerate로 인덱스와 함께 큐에 저장
    q = deque(list(enumerate(priorities)))
    
    count = 0
    # q가 빌 떄까지 반복
    while q:
        idx, j = q.popleft()
        
        find = False
        for x in q:
            if x[1] > j:
                q.append((idx, j))
                find = True
                break
            
        # 찾지 못했다면 j를 인쇄한다
        if not find:
            count += 1
            if idx == location:
                return count