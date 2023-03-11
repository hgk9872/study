# RGB 거리
# https://www.acmicpc.net/problem/1149

n = int(input())

# DP 테이블.. 2차원을 만들어야함
graph = [list(map(int, input().split())) for _ in range(n)]


for i in range(1, n):
    graph[i][0] = graph[i][0] + min(graph[i-1][1], graph[i-1][2])
    graph[i][1] = graph[i][1] + min(graph[i-1][0], graph[i-1][2])
    graph[i][2] = graph[i][2] + min(graph[i-1][0], graph[i-1][1])

print(min(graph[n-1]))
