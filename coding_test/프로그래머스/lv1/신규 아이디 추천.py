# https://school.programmers.co.kr/learn/courses/30/lessons/72410

def solution(new_id):
    
    # 아이디 추천 - 유사하면서 규칙에 맞는 아이디
    
    # 아이디 길이 3 ~ 15
    # 소문자, 숫자, -, _, .
    # .은 처음과 끝에 사용 불가. 연속 불가
    answer = ''
    
    # 1단계
    new_id = new_id.lower()
    
    # 2단계
    for x in new_id:
        if x.isdigit() or x.isalpha() or x == '-' or x == '_' or x == '.':
            answer += x

    # 3단계
    while '..' in answer:
        answer = answer.replace('..', '.')
    
    # 4단계
    if len(answer) >= 2:
        if answer[0] == '.':
            answer = answer[1:]
        if answer[-1] == '.':
            answer = answer[:-1]
    elif answer == '.':
        answer = ''

    # 5단계
    if answer == '':
        answer += 'a'
    
    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
            
    while(len(answer) <= 2):
        answer += answer[-1]

    return answer