# https://school.programmers.co.kr/learn/courses/30/lessons/43164

def solution(tickets):
    # tickets의 각 행 [a, b]는 a 공항 -> b 공항
    # 모두 사용해야 함 -> dfs
    # 만약 경로가 2개 이상일 경우 알파벳 순서로
    # 모든 도시를 방문할 수 없는 경우는 없다
    # 항상 인천공항에서 출발 ("ICN")
    path = ["ICN"]
    visited = [False] * len(tickets)
    path_list = []
    
    def dfs(idx, start, path):
        # 모든 티켓을 사용한 경우 패스 추가
        if idx == len(tickets):
            path_list.append(path)
        
        # 모든 티켓을 순회하면서
        for i, ticket in enumerate(tickets):
            # 아직 방문 안했고, 출발지가 일치
            if not visited[i] and ticket[0] == start:
                visited[i] = True
                dfs(idx + 1, ticket[1], path+[ticket[1]])
                visited[i] = False
                
    
    dfs(0, "ICN", path)
    path_list.sort()
    answer = path_list[0]
    return answer