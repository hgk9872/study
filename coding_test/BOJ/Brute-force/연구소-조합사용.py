# 두 번째 풀이
# 벽을 3개 설치하는 과정을 dfs -> 조합으로 해결
# 이 경우 python3 에서 별도의 추가작업없이 시간초과 안남
# 직관적이고 괜찮은 방법인듯..
from itertools import combinations

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
copy = [[0] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0

# bfs후, count 세서 max값을 answer에 저장
def bfs():
    global answer
    
    virus = [(i, j) for i in range(n) for j in range(m) if copy[i][j] == 2]

    while virus:
        x, y = virus.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and copy[nx][ny] ==0:
                copy[nx][ny] = 2
                virus.append((nx, ny))
    
    zero_count = 0
    for row in copy:
        zero_count += row.count(0)
    answer = max(answer, zero_count)

# 빈 공간(0)에 해당하는 좌표 리스트
empty_list = [(i, j) for i in range(n) for j in range(m) if graph[i][j] == 0]

for comb in combinations(empty_list, 3):
    # 카피본 만들고,
    for i in range(n):
        for j in range(m):
            copy[i][j] = graph[i][j]
    
    # 카피본에 벽 생성
    for x, y in comb:
        copy[x][y] = 1

    bfs()

print(answer)