# 백준 17144 - 골드4
# https://www.acmicpc.net/problem/17144

def spread(arr):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    temp = [] # 미세먼지가 있는 좌표를 담을 리스트
    
    # 미세먼지 좌표들을 리스트에 담는다
    for i in range(n):
        for j in range(m):
            if arr[i][j] != 0 and arr[i][j] != -1:
                temp.append((i, j))

    diff = [[0] * m for _ in range(n)]

    for i in range(len(temp)):
        x, y = temp[i]
        
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
        
            if 0 <= nx < n and 0 <= ny < m: # 좌표계 벗어나지 않고
                if arr[nx][ny] != -1: # 공기청정기가 아니면,
                    diff[nx][ny] += arr[x][y] // 5
                    diff[x][y] -= arr[x][y] // 5
        
    for i in range(n):
        for j in range(m):
            arr[i][j] += diff[i][j]

# 위쪽 공기청정기 바람 순환
def up_circle(up_row):
    # 먼저 위쪽 공기청정기의 바로 오른쪽 부터 시작
    # 방향은 반시계방향으로 지정 
    # 동 -> 북 -> 서 -> 남
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    
    # 첫 번째 구역 청소
    temp = arr[up_row][1]
    arr[up_row][1] = 0

    dir = 0
    x = up_row
    y = 1

    while True:
        nx = x + dx[dir]
        ny = y + dx[dir]

        next = arr[nx][ny]




# 미세먼지 순환, 공기청정기 각각 구현
n, m, t = map(int, input().split()) # 가로, 세로, 초

arr = [list(map(int, input().split())) for _ in range(n)]

cleaner = []
# 각 행에서 공기청정기 찾기
for i in range(n):
    if arr[i][0] == -1:
        cleaner.append(i) # 행 위치만 저장


for i in range(t):
    spread(arr)
    print()
    for row in arr:
        print(*row)
    
    circle_up()
    circle_down()