

n, m = map(int, input().split())
x, y, dir = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 회전 (dir - 1) % 4

cnt = 1
turn_time = 0
visited[x][y] = True

while True:
    dir = (dir - 1) % 4
    print('현재 방향', dir)
    nx = x + dx[dir]
    ny = y + dy[dir]

    if graph[nx][ny] == 0 and not visited[nx][ny]:
        visited[nx][ny] = True
        cnt += 1
        turn_time = 0
        x = nx
        y = ny
        continue
    else:
        turn_time += 1
    
    if turn_time == 4:
        nx = x - dx[dir]
        ny = y - dy[dir]

        if graph[nx][ny] == 1:
            break
        x = nx
        y = ny
        turn_time = 0

print(cnt)