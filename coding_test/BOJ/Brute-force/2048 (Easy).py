# 백준 12100 - 골드2 (브루트포스)
# https://www.acmicpc.net/problem/12100
import copy

# dir : 0, 1, 2, 3 -> 동, 서, 남, 북
def move(graph, dir):
    if dir == 0: # 동
        for i in range(n): # 행
            # 현재 가장 동쪽에 해당하는 idx
            right = n-1
            for j in range(n-2, -1, -1): # 가장 끝의 전칸부터 오른쪽으로 이동
                if graph[i][j]: # 숫자값이 있는 것만 이동
                    temp = graph[i][j]
                    graph[i][j] = 0
                    if graph[i][right] == 0: # 아무 값도 없는 경우 이동만
                        graph[i][right] = temp
                    elif graph[i][right] == temp: # 값이 같은 경우
                        graph[i][right] = temp * 2
                        right = right - 1
                    else: # 다른 숫자인 경우
                        graph[i][right-1] = temp
                        right = right - 1
    
    elif dir == 1: # 서
        for i in range(n):
            left = 0
            for j in range(1, n): 
                if graph[i][j]: 
                    temp = graph[i][j]
                    graph[i][j] = 0
                    if graph[i][left] == 0:
                        graph[i][left] = temp
                    elif graph[i][left] == temp:
                        graph[i][left] = temp * 2
                        left = left + 1
                    else:
                        graph[i][left+1] = temp
                        left = left + 1
    
    elif dir == 2: # 남
        for j in range(n):
            down = n-1
            for i in range(n-2, -1, -1):
                if graph[i][j]:
                    temp = graph[i][j]
                    graph[i][j] = 0
                    if graph[down][j] == 0:
                        graph[down][j] = temp
                    elif graph[down][j] == temp:
                        graph[down][j] = temp * 2
                        down = down - 1
                    else:
                        graph[down - 1][j] = temp
                        down = down - 1

    else:
        for j in range(n):
            top = 0
            for i in range(1, n):
                if graph[i][j]:
                    temp = graph[i][j]
                    graph[i][j] = 0
                    if graph[top][j] == 0:
                        graph[top][j] = temp
                    elif graph[top][j] == temp:
                        graph[top][j] = temp * 2
                        top = top + 1
                    else:
                        graph[top+1][j] = temp
                        top = top + 1
        

def dfs(count, graph):
    global answer
    if count == 5:
        max_val = 0
        for row in graph:
            max_val = max(max_val, max(row))
        answer = max(answer, max_val)
        return
    
    # 동, 서, 남, 북 방향에 대해
    for i in range(4):
        copy_graph = copy.deepcopy(graph) # 현재 그래프를 복사
        move(copy_graph, i) # 복사한 그래프에 대해 각 디렉션마다 전달
        dfs(count+1, copy_graph) # count 증가


n = int(input()) # 보드의 크기

graph = [list(map(int, input().split())) for _ in range(n)]
answer = 0

dfs(0, graph)
print(answer)