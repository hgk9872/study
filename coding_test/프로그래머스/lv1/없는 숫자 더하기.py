def solution(numbers):
    answer = 0
    
    # 0~9까지의 연속적인 숫자배열
    digit = list(range(0,10))

    for d in digit:
        if d not in numbers:
            answer += d
    return answer