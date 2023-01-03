# BOJ 15685 - 드래곤 커브 (골드4)
# 시뮬레이션

# 드래곤 커브의 개수 n
n = int(input())

# 0 <= x <= 100, 0 <= y <= 100 그래프
graph = [[False] * 101 for _ in range(101)]

# 방향 오른쪽, 위, 왼쪽, 아래
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# 드래곤 커브 수행하는 함수
def dragon_curve(x, y, d, g):
    graph[y][x] = True # 초기값
    dir_list = [d] # 초기 방향
    # g세대 반복
    for _ in range(g):
        # 기존 방향 리스트를 거꾸로
        reversed_list = reversed(dir_list)
        for dir in reversed_list:
            if dir == 3:
                dir_list.append(0)
            else:
                dir_list.append(dir + 1)
    # print(dir_list)
    
    # 저장된 방향 리스트를 토대로 커브 수행
    for dir in dir_list:
        x += dx[dir]
        y += dy[dir]
        graph[y][x] = True


for _ in range(n):
    # 시작점 x, y 시작방향 d, 세대 g
    x, y, d, g = list(map(int, input().split()))
    dragon_curve(x, y, d, g)

count = 0

for i in range(100):
    for j in range(100):
        if graph[i][j] == 1 and graph[i+1][j] == 1 \
            and graph[i][j+1] == 1 and graph[i+1][j+1] == 1:
            count += 1

print(count)