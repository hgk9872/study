# https://school.programmers.co.kr/learn/courses/30/lessons/17683
# 호흡이 굉장히 긴 문제.. 노션 정리
# 여기에 나온 여러 문자열 관련 테크닉을 익혀놓자 (특히 시간)

def clean(melody):
    # #이 붙은 음은 소문자로 변경
    if 'C#' in melody:
        melody = melody.replace('C#', 'c')
    if 'D#' in melody:
        melody = melody.replace('D#', 'd')
    if 'F#' in melody:
        melody = melody.replace('F#', 'f')
    if 'G#' in melody:
        melody = melody.replace('G#', 'g')
    if 'A#' in melody:
        melody = melody.replace('A#', 'a')
    
    return melody

def solution(m, musicinfos):
    # 기억하고 있는 멜로디 : 해당 음악의 끝부분과 첫 부분이 이어질 수도 있다
    # 반대로, 음악을 중간에 끊을 경우 아닐수도잇다?
    # 음은 1분에 한개씩, 무조건 처음부터 재생
    # 기억한 멜로디 m
    
    # 먼저, musicinfos에 대해서 각 재생시간에 대한 문자열을 뽑아내보자
    
    # 각 정보에서 시간, 제목, 멜로디 순으로 출력해보기
    clean_info = []
    for row in musicinfos:
        info = row.split(',')
        # 시간 확인하기
        time = (int(info[1][:2]) - int(info[0][:2]))*60 + int(info[1][3:]) - int(info[0][3:])
        
        title = info[2]
        
        melody = clean(info[3])
        
        full_melody = ''
        
        for i in range(time):
            full_melody += melody[i % len(melody)]
            
        # 기억한 멜로디도 clean
        m = clean(m)
        
        if m in full_melody:
            clean_info.append([time, title, full_melody])
            
    print(clean_info)
    if not clean_info:
        return '(None)'
    
    clean_info.sort(key=lambda x:-x[0])
    # 이미 처음에 입력된 대로 데이터가 들어갔으므로, 시간으로 정렬만 하면 끝나는듯...
    answer = clean_info.pop(0)[1]
    
    return answer
