# bfs를 통한 풀이

from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n

    # bfs가 한 번 시행될 때마다, 같은 네트워크를 모두 순회하면서 방문체크됨
    def bfs(start, visited, computers):
        visited[start] = True
        queue = deque([start])
        while queue:
            v = queue.popleft()
            for i in range(n):
                # 방문하지 않은 연결된 컴퓨터
                if computers[v][i] == 1 and not visited[i]:
                    visited[i] = True
                    queue.append(i)

    # 모든 노드 체크하면서, 방문하지 않은 노드에 대해 bfs 시행
    for i in range(n):
        if not visited[i]:
            bfs(i, visited, computers)
            answer += 1

    return answer