# https://school.programmers.co.kr/learn/courses/30/lessons/12946
# 하노이 코드의 경우, 일단 외우고 어느정도 이해를 하는 것이...

def solution(n):
    answer = []
    
    def hanoi(n, start, end, via):
        if n == 1:
            answer.append([start, end])
        else:
            hanoi(n-1, start, via, end)
            answer.append([start, end])
            hanoi(n-1, via, end, start)
    
    hanoi(n, 1, 3, 2)
    return answer