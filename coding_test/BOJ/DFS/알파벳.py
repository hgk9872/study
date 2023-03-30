# 백준 1987 - 골드4

# 빈 알파벳 리스트를 만들어서, 있는지 비교하면 시간초과남
# 알파벳은 26가지로 정해져있으므로, 이를 미리 만들어서 확인시켜주어야 시간 내에 통과
# python3에서는 안됨.. dfs로 pypy에서만 통과
# 인터넷 블로그의 다른 코드들도 python3에서는 대부분 시간초과

def dfs(x, y, alpha, count):
    global answer
    answer = max(answer, count) # 모든 방문에 대해 최댓값을 확인

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if alpha[ord(graph[nx][ny])-ord('A')] == 0:
                alpha[ord(graph[nx][ny])-ord('A')] = 1
                dfs(nx, ny, alpha, count + 1)
                alpha[ord(graph[nx][ny])-ord('A')] = 0

n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
alpha = [0] * 26

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0

alpha[ord(graph[0][0]) - ord('A')] = 1
dfs(0, 0, alpha, 1)

print(answer)