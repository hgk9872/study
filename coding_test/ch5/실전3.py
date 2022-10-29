n, m = map(int, input().split())

graph = []

# 2차원 리스트의 맵 정보 입력받기
for i in range(n):
    graph.append(list(map(int, input())))

count = 0

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return
    # 만약 방문하지 않았다면 재귀함수로 탐색 후 방문처리
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y) # 상
        dfs(x+1, y) # 하
        dfs(x, y-1) # 좌
        dfs(x, y+1) # 우

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            count += 1
            dfs(i, j)

print(count)