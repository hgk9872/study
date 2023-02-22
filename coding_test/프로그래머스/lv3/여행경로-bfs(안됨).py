# 우선순위 큐로 한번 구현해보자...
# 아마 안되는 이유...?


import heapq

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]


def solution(tickets):
    # tickets의 각 행 [a, b]는 a 공항 -> b 공항
    # 모두 사용해야 함 -> dfs
    # 만약 경로가 2개 이상일 경우 알파벳 순서로
    # 모든 도시를 방문할 수 없는 경우는 없다
    # 항상 인천공항에서 출발 ("ICN")

    # path 배열
    path = ["ICN"]

    # 우선순위 큐 h
    # 초기값 설정
    h = []
    heapq.heappush(h, "ICN")

    # 방문함수
    visited = [False] * len(tickets)

    result = []
    while h:
        # 출발지 꺼내서 list에 추가
        now = heapq.heappop(h)
        result.append(now)

        # 만약 모든 path가 완성되면 그만
        if len(result) == len(tickets) + 1:
            print(result)

        # 모든 티켓 순회
        for i, ticket in enumerate(tickets):
            # 방문하지 않았고, 해당 티켓의 출발지가 일치하다면
            if not visited[i] and ticket[0] == now:
                visited[i] = True
                heapq.heappush(h, ticket[1]) # 다음 출발지를 힙에 넣는다(알파벳순)


    return path


solution(tickets)