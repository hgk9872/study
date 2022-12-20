# BOJ 9663 N-Queen

n = int(input())

# 행 방문에 대한 체크리스트
row_visited = [0] * n

# 실제 체스판에 적재되는 행, 열 값
board = [0] * n

count = 0

# 대각선에 대해서 체크
def check(col):
    # 열의 차이 == 행의 차이 같으면 대각선 -> 헷갈려서 코드 그냥 암기
    for i in range(col):
        if col - i == abs(board[col] - board[i]):
            return False

    return True

def dfs(col):
    global count
    if col == n :
        count += 1
        return
    # 방문하지 않은 row에 대해
    for row in range(n):
        if row_visited[row] == 0:
            board[col] = row # 실제 체스판에 값 적재
            if check(col):
                row_visited[row] = 1
                dfs(col + 1)
                row_visited[row] = 0

# 0열부터 시작
dfs(0)

print(count)