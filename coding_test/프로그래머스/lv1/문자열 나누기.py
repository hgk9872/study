# https://school.programmers.co.kr/learn/courses/30/lessons/140108
# 인덱스 에러날까봐 헷갈리게 풀었음
# lv1이지만 좀 헷갈리는 부분이 있다

def solution(s):
    answer = 0

    while s:
        cnt = 0
        for i in range(len(s)):
            # 첫 글자와 같다면
            if s[i] == s[0]:
                cnt += 1
            else: # 다르다면
                cnt -= 1
            
            # 횟수가 같아져서 분리하거나, 만약 두 횟수가 다른 상태에서 더 이상 읽을 글자가 없다면
            if cnt == 0 or i == len(s) - 1:
                answer += 1
                s = s[i+1:] # 인덱스 에러 안남!!
                break
            
    return answer