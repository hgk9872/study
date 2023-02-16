# reverse 익히기 문자열 reversed(문자열) -> ㄹ스트로 나옴 ''.join
# zfill 함수 : 문자열.zfill(5) :> 5자리 숫자
# 2진수 문자열 만드는법 익히기

def solution(n, arr1, arr2):
    
    map1 = []
    for i in arr1:
        line = ''
        count = n
        while True:
            count -= 1
            if i % 2 == 0:
                line += ' '
            else:
                line += '#'
            if i // 2 == 0:
                break
            i = i // 2
        if count > 0:
            line += ' ' * count
        map1.append(''.join(reversed(line)))
    
    map2 = []
    for i in arr2:
        line = ''
        count = n
        while True:
            count -= 1
            if i % 2 == 0:
                line += ' '
            else:
                line += '#'
            if i // 2 == 0:
                break
            i = i // 2
        if count > 0:
            line += ' ' * count
        map2.append(''.join(reversed(line)))
        
    answer = []
    
    for i in range(n):
        line = ''
        for j in range(n):
            if map1[i][j] == '#' or map2[i][j] == '#':
                line += '#'
            else:
                line += ' '
        answer.append(line)
    return answer