n, m = map(int, input().split())
visit = [[0] * m for _ in range(n)]

# 현재위치와 방향(d)
x, y, d = map(int, input().split())
visit[x][y] = 1
# d -> 북:0, 동:1, 남:2, 서:3

# 전체 맵 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 각 인덱스 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전하는 함수
def turn():
    global d
    d -= 1
    if d == -1:
        d = 3

# 시뮬레이션 시작
count = 1
turn_time = 0

while True:
    turn()
    nx = x + dx[d]
    ny = y + dy[d]
    if visit[nx][ny] == 0 and array[nx][ny] == 0:
        visit[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        if array[nx][ny] == 1:
            break
        else:
            x = nx
            y = ny
        turn_time = 0

print(count)
