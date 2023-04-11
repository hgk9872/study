# https://www.acmicpc.net/problem/10709 s5

n, m = map(int, input().split())

graph = [list(input()) for _ in range(n)]
result = [[0] * m for _ in range(n)]

# 구름 좌표 저장
q = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'c':
            q.append((i, j, 0)) # 좌표 리스트에 저장
        else:
            result[i][j] = -1
        

time = 0
# 그래프에 있는 c들을 매 시간마다 오른쪽으로 한칸씩 이동
while q:
    x, y, time = q.pop()
    nx = x
    ny = y + 1
    time += 1
    if 0 <= nx < n and 0 <= ny < m:
        if result[nx][ny] == -1:
            result[nx][ny] = time
            q.append((nx, ny, time))

for row in result:
    print(*row)
