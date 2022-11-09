# 다시 풀고 재채점결과 답은 맞았으나 조금 비효율적인 부분있음
# next, prev 부분..

def solution(s):
    answer = len(s)
    for i in range(1, len(s) // 2 + 1):
        result = ""
        count = 1
        # i단위로 문자열을 자름
        prev = s[0:i]
        for j in range(i, len(s), i):
            next = s[j:j+i]
            if prev == next:
                count += 1
            else:
                if count == 1: # 만약 반복되지 않는다면
                    result += prev
                else: # 여러번 반복되는 경우
                    result += str(count) + prev
                    count = 1
            prev = s[j:j+i]
        if count == 1:
            result += next
        else:
            result += str(count) + prev
            
        answer = min(len(result), answer)
    
    return answer