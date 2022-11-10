# 경쟁적 전염 p344

# 크기 n, 바이러스 번호 최대 k
n, k = map(int, input().split())

# 그래프
graph = []

# 바이러스 정보를 저장하는 그래프
h = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        # 만약 시험관에 바이러스가 있는 칸이라면
        if graph[i][j] != 0:
            # 해당 바이러스의 번호와 좌표 저장
            h.append((graph[i][j], i, j))


# 상 하 좌 우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

s, X, Y = map(int, input().split())

for i in range(s):
    h.sort(key = lambda x:x[0])
    # 바이러스의 번호가 작은 수부터
    for j in range(len(h)):
        data = h.pop(0)
        x = data[1]
        y = data[2]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or ny < 0 or nx >= n or ny >= n or graph[nx][ny] != 0:
                continue
            graph[nx][ny] = graph[x][y]
            h.append((graph[nx][ny], nx, ny))

print(graph[X-1][Y-1])