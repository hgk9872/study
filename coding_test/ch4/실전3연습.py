n, m = map(int, input().split())

# 게임 캐릭터의 시작좌표와 방향
# 0: 북쪽, 1: 동쪽, 2: 남쪽, 3: 서쪽
x, y, direction = map(int, input().split())

# direction
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
