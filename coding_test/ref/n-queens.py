# 내가 작성한 코드 중 가장 깔끔하다고 생각되는 코드
# 어느정도 유형을 외울 필요가 있다

# 들어온 퀸의 위치가 가능한지 체크하는 함수
def check(row, queen):
    # 현재까지의 행 중에서
    for i in range(row):
        # col값이 겹치거나 // 대각선에 겹치면
        if queen[row] == queen[i] or abs(row - i) == abs(queen[row] - queen[i]):
            return False
    
    return True

def dfs(n, row, queen):
    global count
    
    # 만약 모든 행을 순회한 경우 
    if row == n:
        count += 1
        return
    
    # 현재 행의 Q위치 할당
    for col in range(n):
        queen[row] = col
        
        # 현재 퀸이 들어간 위치에 대해서 유망한지 체크
        if check(row, queen):
            dfs(n, row+1, queen)

def solution(n):
    global count
    count = 0
    
    # queen 배열에 Q 위치를 저장
    # 예를들어 queen[0] = 1 이면, 0행 1열에 Q있다는 것
    # queen의 초기값 설정
    queen = [0] * n
    
    
    # dfs 0행부터 시작
    dfs(n, 0, queen)
    
    print(count)
    
    return count