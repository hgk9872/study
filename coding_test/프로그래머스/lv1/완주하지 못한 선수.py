# 해시로 푸는 경우가 있고
# python의 colletions를 이용하는 경우 존재
# collections 이용해서 풀어보기

from collections import Counter

def solution(participant, completion):
    # completion -> 완주한 선수들의 배열
    # participant -> 참여한 선수들의 배열
    p = Counter(participant)
    print(p)
    c = Counter(completion)
    print(c)
    result = p - c
    print(result.keys())
    return list(result.keys())[0]

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

solution(participant, completion)