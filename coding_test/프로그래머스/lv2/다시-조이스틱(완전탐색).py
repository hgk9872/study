# 현재 위치에서 다음 문자를 할 떄 매번 왼쪽출발 오른쪽출발 중 뭐가 큰지 비교하면서?


def solution(name):
    answer = 0
    n = len(name)
    
    # name의 길이만큼 A 배열 만들기
    default = ['A' for _ in range(n)]
    
    i = 0
    while True:
       # 알파벳 최솟값 계산
        answer += min(ord('Z') - ord(name[i]) + 1, ord(name[i]) - ord('A'))
        
        #해당 알파벳으로 해당 위치 바꿔줌
        default[i] = name[i]
        
        #만약에 문자열이 완성되었다면 종료
        if ''.join(default) == name:
            return answer
        
        # 현재 위치에서 왼쪽으로 이동해서 다음 위치 찾을 경우 카운트
        left = i
        left_cnt = 0
        while default[left] == name[left]:
            left = (left - 1) % n
            left_cnt += 1
        
        # 현재 위치에서 오른쪽으로 이동해서 다음 위치 찾을 경우 카운트
        right = i
        right_cnt = 0
        while default[right] == name[right]:
            right = (right + 1) % n
            right_cnt += 1
        
        # 둘 중에 더 작은 값으로 현재 인덱스 바꿔주고 
        # 카운트한 값 answer에 더하기
        if left_cnt < right_cnt:
            i = left
            answer += left_cnt
        else:
            i = right
            answer += right_cnt
    return answer 