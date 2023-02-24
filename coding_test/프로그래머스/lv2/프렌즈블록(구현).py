# https://school.programmers.co.kr/learn/courses/30/lessons/17679
# 알고리즘 자체가 엄청 어렵진 않음. 대신 구현이 좀 번거롭다
# 이런 문제들은 연습을 많이 하는 방법 밖에 없는 듯. 그리고 조건 주의하기

def solution(m, n, board):
    # 행 m, 열 n
    # 발견할때마다 지우면 안됨.
    # 1. 모두 확인하고 한 번에 지우기... -> stack? 
    # 2. 지운다고 하면.. 그 다음 내려오게 하기
    
    map = []
    for row in board:
        map.append(list(row))
    
    answer = 0
    
    stack = []
    
    while True:
        # 1번 과정
        for i in range(1, m):
            for j in range(1, n):
                if map[i][j] == 0: continue
                if map[i][j] == map[i][j-1] == map[i-1][j] == map[i-1][j-1]:
                    stack.append((i, j))

        # 없으면 끝
        if not stack:
            count = 0
            for i in range(m):
                for j in range(n):
                    if map[i][j] == 0:
                        count += 1
            return count
    
        ## 2번과정 있으면 해당 원소를 처리
        # 먼저 지우고,
        while stack:
            i, j = stack.pop()
            map[i][j] = 0
            map[i-1][j] = 0
            map[i-1][j-1] = 0
            map[i][j-1] = 0
        
        # 남은 부분을 채운다
        
        # 각 열마다 땡기기
        for j in range(n):
            # 아랫쪽 행부터 시작
            for i in range(m-1, -1, -1):
                if map[i][j] == 0:
                    ni = i - 1
                    while ni >= 0:
                        if map[ni][j] != 0:
                            map[i][j] = map[ni][j]
                            map[ni][j] = 0
                            break
                        ni -= 1