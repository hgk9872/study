#

# 1. 한 번에 한 개의 알파벳만 변환할 수 있다
# 2. words에 있는 알파벳만 변환할 수 있다

# "hit"  "cog"	 ["hot", "dot", "dog", "lot", "log", "cog"]

from collections import deque

# 문자열 하나만 다르면 true를 리턴,
# 모든 문자열의 길이는 같다
def compare(origin, word):
    n = len(origin)
    
    diff_count = 0
    # 문자열의 각 문자들을 비교
    for i in range(n):
        if origin[i] != word[i]:
            diff_count += 1
    
    # 문자 하나만 다르다면, 참 리턴
    if diff_count == 1:
        return True
    else:
        return False


def change(begin, target, words):
    
    if target not in words:
        return 0
    
    q = deque()
    q.append((begin, 0))

    # bfs 시작
    while q:
        now, count = q.popleft()

        if now == target:
            return count

        for i in range(len(words)):
            next = words[i] # 다음 단어
            # 한 문자만 바꿔서 next와 같다면, count 증가시켜 bfs
            if compare(now, next):
                q.append((next, count+1))


def solution(begin, target, words):

    answer = change(begin, target, words)
    return answer