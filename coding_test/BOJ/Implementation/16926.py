# BOJ 16926 - 배열 돌리기 (실버1)
# 구현 문제

import sys
input = sys.stdin.readline

# 배열 크기 n, m 회전 수 r
n, m, r = map(int, input().split())

# 주어진 배열
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

# 각각 좌, 하, 우, 상 위치에서 이동하는 방향
# 아래, 오른쪽, 위, 왼쪽으로 move
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
# 회전 구현
# 좀 나중에

# 한번 회전하는 코드
def rotate(i):
    # 주어진 x, y값 : 현재 돌고있는 사각형의 가장 왼쪽 위 (0, 0)
    x, y = i, i
    pre = arr[x][y]
    # 방향이동
    for d in range(4):
        # 경계선에 이를때까지 계속 값 옮긴다
        while True:
            nx = x + dx[d]
            ny = y + dy[d]
            # 만약 범위를 벗어나면
            if nx < i or ny < i or nx >= n-i or ny >= m-i:
                # 한 칸을 복귀시키고
                x = nx - dx[d]
                y = ny - dy[d]
                break
            # 범위가 벗어나지 않을 때 까지 한칸씩 이동
            temp = arr[nx][ny] # 현재 값 저장
            arr[nx][ny] = pre  # 이전값 입력 (한칸 move)
            pre = temp
            x = nx
            y = ny


# r번 회전하기
for _ in range(r):
    # 가장 바깥 영역부터 안까지 들어가면서 모두 회전시키기
    for i in range(min(n, m) // 2):
        rotate(i)

for row in arr:
    print(*row)