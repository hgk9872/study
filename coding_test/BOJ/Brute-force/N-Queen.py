# 백준 9663 - 골드4
# https://www.acmicpc.net/problem/9663

# True면 놓고, False면 놓을 수 없음
def check(x, y):
    if x == 0:
        return True
    else:
        return False

def dfs(cnt):
    global answer

    # 퀸을 N개 다 놓을 수 있다면 경우의 수 +1 증가
    if cnt == n:
        answer += 1
        print(graph)
        return
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0:
                if check(i, j):
                    graph[i][j] = 1
                    dfs(cnt + 1)
                    graph[i][j] = 0


n = int(input())

graph = [[0] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]

answer = 0
dfs(0) # 퀸의 개수를 전달

print(answer)
