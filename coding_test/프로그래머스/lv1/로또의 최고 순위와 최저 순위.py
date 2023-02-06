# https://school.programmers.co.kr/learn/courses/30/lessons/77484#fn1

def solution(lottos, win_nums):
    
    # 구매한 로또 번호 리스트
    # 로또 당첨 번호 리스트
    
    # 0일 때 다 당첨 -> 최고 순위
    # 0일 때 다 당첨X -> 최저 순위
    
    zero_count = 0
    lotto_count = 0
    answer = []
    
    for num in lottos:
        if num in win_nums:
            lotto_count += 1
        elif num == 0:
            zero_count += 1
    
    # 최고 순위
    max_rank = 7 - lotto_count - zero_count
    # rank가 6이상인 경우 -> 순위 6 고정
    if max_rank >= 6:
        answer.append(6)
    else:
        answer.append(max_rank)
    
    min_rank = 7 - lotto_count

    # 최저 순위
    if min_rank >= 6:
        answer.append(6)
    else:
        answer.append(min_rank)
    
    return answer