# https://school.programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    # 숫자-영단어 사전만들어서
    # 해당 영단어가 주어진 s에 있으면 숫자로 변환
    # 그리고 전부 바꿔지면 그 문자열 s를 int로
    
    # 숫자-영단어 사전 만들기
    digit_dict = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }

    for word, digit in digit_dict.items():
        if word in s:
            s = s.replace(word, digit)
    
    answer = int(s)
    return answer