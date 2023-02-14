# 그리디

def solution(n, lost, reserve):
    # 마지막 조건을 고려해서 다시 정의한 lost, reserver 리스트
    reserve_list = [r for r in reserve if r not in lost]
    lost_list = [l for l in lost if l not in reserve]

    # 위 두 방법으로 리스트를 다시 정의해야만 모든 테스트에서 통과한다
    # 위 처럼 리스트컴프리헨션 익히기
    # for문으로 하나씩 remove했을 때는 틀림 (??)

    for r in reserve_list:
        if r-1 in lost_list:
            lost_list.remove(r-1)
        elif r+1 in lost_list:
            lost_list.remove(r+1)
    return n - len(lost_list)