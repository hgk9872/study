# BOJ 20055 - 배열 돌리기 (골드5)
# 구현

import sys
from collections import deque
input = sys.stdin.readline

# 내리는 위치 n번칸, 내구도가 0인 칸의 개수의 max값 k
n, k = map(int, input().split())

# 전체 리스트의 내구도
data = list(map(int, input().split()))
belt = deque(data)

# 로봇이 칸에 존재하는지 여부에 대한 리스트
robot = deque([False] * n)

step = 1
while True:
    ### 1. 로봇과 함께 벨트 회전
    # 벨트 회전
    belt.appendleft(belt.pop())
    # 로봇 회전
    robot.appendleft(robot.pop())
    robot[n-1] = False # 내리는 위치에 해당하는 로봇을 내림

    ### 2. 가장 먼저 벨트에 올라간 로봇부터,
    ### 벨트가 회전하는 방향으로 한 칸 이동
    for i in range(n-2, -1, -1):
         # 로봇이 없고, 내구도가 1 이상이면
        if robot[i] and not robot[i+1] and belt[i+1] >= 1:
            robot[i+1] = True
            robot[i] = False
            belt[i+1] -= 1
    # 내리는 위치에 해당하는 로봇을 내림
    robot[n-1] = False

    ### 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면
    ### 올리는 위치에 로봇을 올린다
    if belt[0] != 0:
        robot[0] = True
        belt[0] -= 1
    
    ### 내구도가 0인 칸의 개수가 k개 이상이라면 과정 종료한다
    if belt.count(0) >= k:
        break
    step += 1

print(step)