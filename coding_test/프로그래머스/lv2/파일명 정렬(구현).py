# https://school.programmers.co.kr/learn/courses/30/lessons/17686
# 예외처리 안해서 틀릴뻔함

def solution(files):
    # 영문 대소문자, 숫자, 공백(" "), 마침표("."), 빼기 부호("-")
    
    # 정렬을 위한 리스트를 만들고.. (인덱스 포함)
    # 거기서 인덱스만 뽑아내서 files 만들어서 리턴
    
    full_list = []
    
    for i, data in enumerate(files):
        print(i, data)
        # 각 데이터마다 분리....
        
        # HEAD 문자 / 한글자이상 /
        number_idx = 0
        for j in range(len(data)):
            # 숫자가 나올 때까지
            if data[j].isdigit():
                number_idx = j
                break
        
        head = data[:number_idx]
        
        # NUMBER 무조건 숫자
        tail_idx = -1
        for j in range(number_idx, len(data)):
            if not data[j].isdigit():
                tail_idx = j
                break
        
        # tail이 없을 경우 tail_idx 값이 계산되지 않는다.
        if tail_idx == -1:
            number = data[number_idx:]
            tail = ''
        else:
            number = data[number_idx:tail_idx]
            tail = data[tail_idx:]
 
        full_list.append([i, data, head.lower(), int(number), tail])
    
    full_list.sort(key=lambda x: (x[2], x[3], x[0]))
    
    answer = []
    
    for x in full_list:
        answer.append(x[1])
    
    return answer