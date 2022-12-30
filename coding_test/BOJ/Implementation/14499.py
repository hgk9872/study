# BOJ 14499 - 주사위 굴리기 (골드4)

# 세로 n, 가로 m, 주사위 좌표 x, y, 명령수 k
n, m, x, y, k = map(int, input().split())

# 주어진 지도
arr = []
for _ in range(n):
    data = list(map(int, input().split()))
    arr.append(data)

# 명령입력 (1: 동, 2: 서, 3: 북, 4: 남)
direction_list = list(map(int, input().split()))

# direction 동 서 북 남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 주사위 = 위, 아래, 왼, 오, 앞, 뒤
dice = [0, 0, 0, 0, 0, 0]

# 맨 처음 아래에(인덱스 1) 입력되는 값
dice[1] = arr[x][y]

# 방향 이동할 때 마다
for i in direction_list:
    nx = x + dx[i-1]
    ny = y + dy[i-1]
    # 바깥으로 이동시키려고 하는 경우
    if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
    # 현재 주사위 값
    u, d, l, r, f, b = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]

    # 명령 방향
    if i == 1: # 동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = l, r, d, u, f, b
    elif i == 2: # 서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = r, l, u, d, f, b
    elif i == 3: # 북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = f, b, l, r, d, u
    else: # 남
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, l, r, u, d

    # 이동하고나서 연산
    if arr[nx][ny] == 0:
        arr[nx][ny] = dice[1] # 아랫면 값 복사
    else:
        dice[1] = arr[nx][ny]
        arr[nx][ny] = 0
    print(dice[0])
    x, y = nx, ny