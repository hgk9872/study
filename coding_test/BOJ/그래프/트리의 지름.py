# 백준 1167 - 골드2
# 트리의 지름을 구하는 방법에 대해서 알아야만 풀 수 있음
# 이 부분은 증명까지 필요하므로, 연습용으로만 풀자

import sys
sys.setrecursionlimit(10**6)

def main():
    v = int(input())
    graph = [[] for _ in range(v+1)]

    # 방문체크 위한 리스트와 거리정보를 저장하는 리스트를 각각 만들어야 함
    visited = [False] * (v+1)
    distances = [0] * (v+1)

    for _ in range(v): # 그래프 입력 받기
        temp = list(map(int,sys.stdin.readline().strip().split()))
        start = temp[0]
        for i in range(1, len(temp)-1, 2):
            graph[start].append((temp[i], temp[i+1]))

    dfs(1, graph, visited, distances) # 임의의 시작 노드에서 가장 먼 노드

    u = max(range(1,v+1), key=lambda x: distances[x]) # 거리가 가장 먼 노드

    visited = [False] * (v+1) # 초기화
    distances = [0] * (v+1)

    dfs(u, graph, visited, distances) # 가장 먼 노드에서 다시 탐색

    v = max(range(1,v+1), key=lambda x: distances[x]) # 가장 먼 노드

    print(distances[v])

def dfs(node, graph, visited, distances):
    visited[node] = True
    for neighbor, weight in graph[node]:
        if not visited[neighbor]:
            distances[neighbor] = distances[node] + weight
            dfs(neighbor, graph, visited, distances)

if __name__ == '__main__':
    main()
