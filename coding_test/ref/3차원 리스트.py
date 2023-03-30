
m, n, h = map(int, input().split())

graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

# graph의 첫 번째 부분이 높이가 됨
# 즉, graph[h][n][m] 이라는 것... z, x, y 순서
print(graph[0])
print(graph[1])