def solution(N, stages):
    # 전체 스테이지 개수 N, 현재 사용자가 멈춰있는 스테이지 번호배열 stages
    # 기수정렬
    
    # 스테이지에 머무른 사람들의 수에 대한 리스트
    count_list = [0] * (N + 2)
    
    # 스테이지의 각 원소마다 카운트 리스트에 저장
    for x in stages:
        count_list[x] += 1
    
    total = len(stages)
    
    result = []
    # 스테이지 번호 i
    for i in range(1, N + 1):
        if count_list[i] == 0:
            rate = 0
        else:
            rate = count_list[i] / total # 실패율
        total -= count_list[i] # 다음 스테이지에서 사용할 분모값
        result.append((i, rate))
    
    result.sort(reverse=True, key=lambda x:x[1])
    
    answer = [i[0] for i in result]
    
    return answer