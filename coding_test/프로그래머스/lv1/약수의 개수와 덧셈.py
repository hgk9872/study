# https://school.programmers.co.kr/learn/courses/30/lessons/77884

# 약수의 개수를 리턴하는 함수
def check(number):
    count = 0
    
    # 약수 개수 count
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1
            
    return count

def solution(left, right):
    
    answer = 0
    
    for number in range(left, right + 1):
        if check(number) % 2 == 0: # 짝수
            answer += number
        else: # 홀수
            answer -= number
    
    return answer