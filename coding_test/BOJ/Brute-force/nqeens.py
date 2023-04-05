n = int(input())
answer = 0
rows = [0] * n

# 현재 놓은 퀸 자리가 유효한지 체크
def is_valid(r):
    for i in range(r):
        # 세로 체크
        if rows[i] == rows[r]:
            return False
        # 대각선 체크
        if abs(r - i) == abs(rows[r] - rows[i]):
            return False
    return True

# r행에 퀸을 놓아보기
def put_queen(r):
    global answer
    if r == n:
        answer += 1
        return
    
    for i in range(n):
        rows[r] = i # r번 째 행에 대해서 i번째 열에 위치 시킨다
        if is_valid(r):
            # 해당 자리에 놓을 수 있다면 다음행으로!
            put_queen(r + 1)
    
put_queen(0)
print(answer)