# 백준 1080 - 실버1
# https://www.acmicpc.net/problem/1080
# 그리디(?)

# 시작점(i, j)의 3x3에 해당하는 행렬을 뒤집음
def change(i, j):
    for x in range(i, i + 3):
        for y in range(j, j + 3):
            graph1[x][y] = 1 - graph1[x][y]


# 행렬의 크기
n, m = map(int, input().split())

graph1 = [list(map(int, input())) for _ in range(n)]
graph2 = [list(map(int, input())) for _ in range(n)]

count = 0

# 그래프 내에서 3x3만큼 바꿀수 있는 모든 위치를 찾고 뒤집음
for i in range(n-2):
    for j in range(m-2):
        if graph1[i][j] != graph2[i][j]: # 해당 원소가 다를 때만 뒤집는 작업 수행
            change(i, j)
            count += 1

# 이후 두 그래프가 같은지 검사
for i in range(n):
    for j in range(m):
        if graph1[i][j] != graph2[i][j]:
            print(-1)
            exit()

# 모든 원소 체크 후, 뒤집은 횟수 출력
print(count)
