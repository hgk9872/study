# dfs 백트래킹

def dfs(start, now, cnt, cost):
    global answer
    if cnt == n:
        if graph[now][start] != 0: # 이 조건 안넣으면 틀린다!!!
            answer = min(answer, cost + graph[now][start])
            return
    
    # 이 조건 넣어줄 경우 좀 빨라짐
    if cost > answer:
        return
    
    for i in range(n):
        # 방문하지 않았고, 갈 수 있는 노드의 경우
        if not visitied[i] and graph[now][i] != 0:
            visitied[i] = True
            dfs(start, i, cnt + 1, cost + graph[now][i]) # 현재 노드에서 다른 노드로 가는 비용을 더해줌
            visitied[i] = False

n = int(input())

# temp = []
visitied = [False] * n
answer = 1e9
graph = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    visitied[i] = True
    dfs(i, i, 1, 0)
    visitied[i] = False

print(answer)