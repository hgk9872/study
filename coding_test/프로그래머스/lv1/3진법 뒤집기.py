# https://school.programmers.co.kr/learn/courses/30/lessons/68935

def solution(n):
    # 주어진 수 n
    
    answer = 0
    temp = []
    
    # 3진법 리스트
    while n > 0:
        temp.append(n % 3)  # 나머지
        n = n // 3          # 몫으로 다음 수 갱신
    
    # 순서 뒤집음 ('0021' --> '1200')
    temp.reverse()
    
    # 첫 번째 인덱스부터 3진법 계산
    for i in range(len(temp)):
        answer += (3**i)*temp[i]

    return answer