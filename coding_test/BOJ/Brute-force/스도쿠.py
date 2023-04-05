# 백준 2580 - 골드4
# https://www.acmicpc.net/problem/2580

def check_row(row, val):
    if val in graph[row]:
        return False
    return True

def check_col(col, val):
    for i in range(9):
        if graph[i][col] == val:
            return False
    return True

def check_rect(x, y, val):
    x = (x // 3)*3
    y = (y // 3)*3
    for i in range(x, x+3):
        for j in range(y, y+3):
            if graph[i][j] == val:
                return False
    return True

def dfs(idx):
    if idx == len(blank):
        for i in range(9):
            print(*graph[i])
        exit()
    
    x, y = blank[idx]
    for i in range(1, 10): # 1~9 값들 중
        if check_row(x, i) and check_col(y, i) and check_rect(x, y, i):
            graph[x][y] = i
            dfs(idx+1)
            graph[x][y] = 0


# 스도쿠 그래프
graph = [list(map(int, input().split())) for _ in range(9)]
blank = [(i, j) for i in range(9) for j in range(9) if graph[i][j] == 0]

dfs(0)
