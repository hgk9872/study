# https://school.programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    # 놀이기구 이용료 N번째 이용하면 원래 이용료 N배
    
    # price : 이용료
    # money : 처음 가지고 있던 금액
    # count : 놀이기구를 이용한 횟수
    # 리턴값 => 부족한 금액
    
    answer = -1

    sum = 0
    for i in range(1, count + 1):
        sum += i * price
    
    short_sum = sum - money
    
    if short_sum >= 0:
        answer = short_sum
    else:
        answer = 0
    
    
    return answer