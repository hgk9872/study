# https://school.programmers.co.kr/learn/courses/30/lessons/17682

def solution(dartResult):
    score_list = []
    idx = 0
    ## 이 부분 기억해두기 ...
    dartResult = dartResult.replace('10','A')
    for i in dartResult:
        # 만약 i가 숫자면 각 세트의 점수
        if i.isdigit() or i == 'A':
            if i == 'A':
                score_list.append(10)
            else:
                score_list.append(int(i))
        elif i in ['S', 'D', 'T']: # 보너스라면
            if i == 'S':
                score_list[idx] = score_list[idx] ** 1
            elif i == 'D':
                score_list[idx] = score_list[idx] ** 2
            else:
                score_list[idx] = score_list[idx] ** 3
            idx += 1
        else: # 옵션
            if i == '*':
                if idx > 1:
                    score_list[idx-1] = score_list[idx-1] * 2
                    score_list[idx-2] = score_list[idx-2] * 2
                else:
                    score_list[idx-1] = score_list[idx-1] * 2
            else:
                score_list[idx-1] = -score_list[idx-1]
        
    print(score_list)
    answer = 0
    return sum(score_list)