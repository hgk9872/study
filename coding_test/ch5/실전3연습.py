# 아이스크림의 개수
# 0으로 되어있는 부분 -> 방문처리 자체를 1로 변경
# 만약 더 이상 스택에서 꺼낼 게 없다면 -> count 증가
# 스택은 리스트로 구현
# 2차원 리스트 그래프...

# 세로의 길이 n, 가로의 길이 m 입력받기
n, m = map(int, input().split())

# 2차원 리스트 생성 및 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 방향이동용 그래프 상하좌우
dx = [-1, 1, 0, 0] # 행방향
dy = [0, 0, -1, 1] # 열방향

count = 0

# DFS 구현
def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return
    if graph[x][y] == 0:
        graph[x][y] = 1 # 방문처리
        for i in range(4): # 상하좌우 방문
            dfs(x + dx[i], y + dy[i])

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            continue
        else:
            count += 1
            dfs(i, j)

print(count)
