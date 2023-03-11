## 첫 번째 풀이.. 조합 없이 풀기
# 완전탐색을 dfs로 하니까 시간이 오래걸림 -> pypy3 에서만 통과
# 벽에 3개 설치하기
def make_wall(cnt):
    if cnt == 3:
        bfs()
        return
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                make_wall(cnt + 1)
                graph[i][j] = 0

# bfs후, count 세서 max값을 answer에 저장
def bfs():
    global answer

    # 복사본 생성 // 또는 copy 함수를 써도 됨
    for i in range(n):
        for j in range(m):
            copy[i][j] = graph[i][j]
    
    virus = [(i, j) for i in range(n) for j in range(m) if graph[i][j] == 2]

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


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
copy = [[0] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0
make_wall(0)
print(answer)