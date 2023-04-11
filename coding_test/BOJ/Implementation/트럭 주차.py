# https://www.acmicpc.net/problem/2979
# 브2

a, b, c = map(int, input().split())

# 해당 시간에 주차되어있는 트럭 수
truck = [0] * 101

for _ in range(3):
    start, end = map(int, input().split())
    for i in range(start, end):
        truck[i] += 1

answer = 0
for i in range(1, 101):
    if truck[i] == 1:
        answer += a
    elif truck[i] == 2:
        answer += b*2
    elif truck[i] == 3:
        answer += c*3

print(answer)