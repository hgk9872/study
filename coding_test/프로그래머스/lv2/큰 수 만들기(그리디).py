# https://school.programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    # 한 글자씩 도는데, 스택에서 해당 글자보다 작은 값이 있으면 횟수만큼 제거
    # 스택에 있는 값이 클 경우 그 값을 넣고 다음 단계로 진행
    if k == 0:
        return number
    
    number = list(number)
    
    stack = [number.pop(0)]
    
    for now in number:
        # 스택에 값이 있고, 아직 뺄 횟수가 남아있으면 처리
        while stack and k > 0 and now > stack[-1]:
            stack.pop()
            k -= 1
        stack.append(now)
    
    # 그래도 k가 남아있다면 그 숫자만큼 뒷부분 잘라내기
    if k > 0:
        stack = stack[:-k]
    
    return ''.join(stack)