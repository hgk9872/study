# BOJ 14503 - 주사위 굴리기 (골드5)

# 세로 크기 n, 가로 m
n, m = map(int, input().split())

# 로봇 청소기의 좌표 (r, c) 현재 방향 d
r, c, d = map(int, input().split())

# 방향 0: 북, 1: 동, 2: 남, 3: 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 지도 
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

result = 0

# 현재 위치 r, c, d 에서 시작
arr[r][c] = -1 # 방문체크
result += 1

while True:
    # 각 방향에 대한 탐색 count
    dir_count = 0
    # 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색
    for _ in range(4):
        # nd는 다음 왼쪽 방향
        nd = (d - 1) % 4
        # 그 방향의 청소공간
        nr = r + dx[nd]
        nc = c + dy[nd]

        if arr[nr][nc] == 0: # 청소공간이 존재하면
            result += 1
            arr[nr][nc] = -1 # 방문체크
            r, c, d = nr, nc, nd
            break
        else: # 청소공간 없다면
            d = nd # 방향만 회전
            dir_count += 1

    # 네 방향 모두 청소가 이미 되어있거나 벽인 경우,
    if dir_count == 4:
        # 현재 방향에서 뒤쪽 방향으로 이동
        r = r + dx[d-2]
        c = c + dy[d-2]
        # 만약 뒤쪽 방향이 벽이라면
        if arr[r][c] == 1:
            break

print(result)