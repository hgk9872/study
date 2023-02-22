# https://school.programmers.co.kr/learn/courses/30/lessons/43165
# dfs를 이용한 정석 풀이
# 백트래킹 방법과 유사

def dfs(index, now, numbers, target):
    global count
    # 모든 연산을 하고, 타겟 넘버가 됐다면 count 증가
    if index == len(numbers):
        if now == target:
            count += 1
    else:
        dfs(index + 1, now + numbers[index], numbers, target)
        dfs(index + 1, now - numbers[index], numbers, target)

# numbers 리스트와 target 값은 인자로 넘어오므로, global 변수 선언 불가
# 따라서 numbers와 target은 dfs 인자로 넘겨주어야 함
# count는 안 넘겨주고 global 변수로 사용 가능
def solution(numbers, target):
    global count
    
    count = 0
    
    dfs(0, 0, numbers, target)
    
    return count