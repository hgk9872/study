# 뱀
from collections import deque

# 보드의 크기 N * N
n = int(input())

# 사과의 개수 k
k = int(input())

graph = [[0] * (n + 1) for i in range(n + 1)]
# 각 사과가 위치한 위치
for _ in range(k):
    a, b = map(int, input().split())
    graph[a][b] = 1 # 사과가 존재하면 1

# X초가 끝난 뒤에 회전시킬 정보를 담은 리스트
seconds = [0] * 10001

# 데이터 입력받아 리스트에 저장
l = int(input())
for _ in range(l):
    data = input().split()
    x = int(data[0])
    seconds[x] = data[1]

# 방향을 나타내는 리스트 0 : 오른쪽, 1 : 아래, 2: 왼쪽, 3: 위
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 초기 설정
graph[1][1] = -1  # 몸이 있는 곳을 -1로 표시
direction = 0 # 시작 방향은 오른쪽(0)
x = 1
y = 1

queue = deque()
queue.append((1, 1)) # 몸통리스트
# 게임 시작
for i in range(1, 10001):
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    # 몸을 만나거나, 벽을 만나면 탈출
    if nx > n or ny > n or nx < 1 or ny < 1 or graph[nx][ny] == -1:
        break

    # 사과가 없는 경우
    if graph[nx][ny] != 1:
        # 큐에서 꼬리를 꺼내 0으로 초기화
        tx, ty = queue.popleft()
        graph[tx][ty] = 0
    
    # 이동할 칸에 머리를 다음에 위치
    graph[nx][ny] = -1
    # 큐에 삽입
    queue.append((nx, ny))
    x, y = nx, ny

    # i초가 끝난 뒤에 회전방향 결정
    if seconds[i] == "L":
        direction -= 1
    # 만약 오른쪽 방향을 보고있을 때, L이 오면 위쪽방향으로 변환
        if direction == -1:
            direction = 3
    elif seconds[i] == "D":
        direction += 1
        if direction == 4:
            direction = 0

print(i)
