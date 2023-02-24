# https://school.programmers.co.kr/learn/courses/30/lessons/42842

def find_pair(num, brown):
    
    candidates = []
    
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            candidates.append((num // i, i))
    
    while candidates:
        m, n = candidates.pop()
        if (m*2 + n*2) == (brown - 4) :
            return m+2, n+2

def solution(brown, yellow):
    
    # 약수 쌍 구하는 방법만 알면 풀 수 있음

    return find_pair(yellow, brown)