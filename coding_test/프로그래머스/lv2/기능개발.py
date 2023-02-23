# https://school.programmers.co.kr/learn/courses/30/lessons/42586
# 자료구조 문제, 큐
# 난이도 있는 자료구조 문제의 경우, 조건을 잘 체크해야함

def solution(progresses, speeds):
    # 큐
    # deque를 사용해서
    # 매번 뽑았다가 다시 넣는 방식을 해보자
    answer = []
    while progresses:
        
        count = 0
        # 현재 가장 첫 번째 기능이 완성되었다면
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        
        # 만약 배포가 되었다면 (count가 증가했다면)
        if count > 0:
            answer.append(count)
        
        # 작업 진행
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
            
    return answer